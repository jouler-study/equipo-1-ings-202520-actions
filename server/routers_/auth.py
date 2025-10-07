# auth.py
"""
Authentication routes: login, logout and token-protected utilities.
"""

from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from pydantic import BaseModel, EmailStr
from passlib.hash import argon2
from datetime import datetime, timedelta
from typing import Optional
from jose import JWTError
from jwt_manager import create_access_token, verify_token
from fastapi import Header
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Security
from utils.email_utils import enviar_correo_bloqueo


router = APIRouter(prefix="/auth", tags=["Auth"])

# In-memory blacklist for invalidated tokens (valid only while server runs)
TOKEN_BLACKLIST: set[str] = set()


# ===============================
# DATABASE DEPENDENCY
# ===============================
# Provides a database session for route handlers.
# Each request gets its own session, closed automatically after completion.
def get_db():
    """
    Provide a DB session to route handlers.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ===============================
# REQUEST MODELS
# ===============================
# Defines the expected structure for login requests.
class UserLogin(BaseModel):
    """
    Input data for login.
    """
    correo: EmailStr
    contrasena: str


# ===============================
# HELPER FUNCTIONS
# ===============================
# Helper functions for token extraction, validation, and blacklist checking.
def get_bearer_token(authorization_header: Optional[str]) -> Optional[str]:
    """
    Extract the Bearer token from Authorization header.
    """
    if not authorization_header:
        return None
    if not authorization_header.startswith("Bearer "):
        return None
    return authorization_header.split(" ", 1)[1].strip()


def check_token_not_blacklisted(token: str):
    """
    Verify that the token is not blacklisted.
    """
    if token in TOKEN_BLACKLIST:
        raise HTTPException(status_code=401, detail="Token inválido (logout requerido)")


def get_current_user_from_token(authorization: Optional[str] = Header(None)) -> dict:
    """
    Validate the Authorization header and return the decoded token payload.
    Raises HTTPException if invalid or expired.
    """
    token = get_bearer_token(authorization)
    if not token:
        raise HTTPException(status_code=401, detail="Token no proporcionado")

    check_token_not_blacklisted(token)

    try:
        payload = verify_token(token)
    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")

    if "sub" not in payload:
        raise HTTPException(status_code=401, detail="Token inválido: falta información")
    return payload


# ===============================
# LOGIN ENDPOINT
# ===============================
# Authenticates a user and returns a valid JWT token.
# Locks the account for 15 minutes after 3 failed attempts.
# Resets failed attempts after successful login.
# Sends an email notification when the account is locked.
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Authenticate user and return a valid JWT token.
    - Temporary lock after 3 failed login attempts (15 minutes).
    - Reset failed attempts after successful login.
    - Send email notification on account lock.
    """
    # Search user by email
    usuario = db.query(Usuario).filter(Usuario.correo == user.correo).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    # Check if account is temporarily locked
    if usuario.cuenta_bloqueada_hasta and usuario.cuenta_bloqueada_hasta > datetime.utcnow():
        raise HTTPException(
            status_code=403,
            detail="Cuenta bloqueada temporalmente. Revisa tu correo."
        )

    # Verify password
    if not argon2.verify(user.contrasena, usuario.contrasena_hash):
        usuario.intentos_fallidos = (usuario.intentos_fallidos or 0) + 1

        # Lock account after 3 failed attempts
        if usuario.intentos_fallidos >= 3:
            usuario.cuenta_bloqueada_hasta = datetime.utcnow() + timedelta(minutes=15)
            db.commit()

            # 🔔 Send account lock notification email
            enviar_correo_bloqueo(usuario.correo, usuario.nombre)

            raise HTTPException(
                status_code=403,
                detail="Cuenta bloqueada por múltiples intentos. Revisa tu correo."
            )

        db.commit()
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")

    # Reset counters after successful login
    usuario.intentos_fallidos = 0
    usuario.cuenta_bloqueada_hasta = None
    db.commit()

    # Create JWT token with user data
    role = usuario.rol if hasattr(usuario, "rol") else "usuario"
    token_data = {"sub": usuario.correo, "rol": role}
    token = create_access_token(data=token_data)

    return {
        "message": "Inicio de sesión exitoso",
        "usuario": usuario.correo,
        "rol": role,
        "access_token": token,
        "token_type": "bearer"
    }


# ===============================
# LOGOUT ENDPOINT
# ===============================
# Invalidates the user's JWT by adding it to a temporary in-memory blacklist.
security = HTTPBearer()

@router.post("/logout")
def logout(credentials: HTTPAuthorizationCredentials = Security(security)):
    """
    Invalidate the JWT received in the Authorization header.
    Must be sent in the format: Bearer <token>.
    """
    token = credentials.credentials  # Extract token automatically

    if token in TOKEN_BLACKLIST:
        raise HTTPException(status_code=400, detail="El token ya fue invalidado")

    TOKEN_BLACKLIST.add(token)

    return {"message": "Sesión cerrada correctamente"}
