from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from pydantic import BaseModel, EmailStr
from passlib.hash import argon2
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth")

def get_db():
    """
    Yields a database session for use in dependency injection.

    This generator function creates a new SQLAlchemy session, yields it for use in
    request handling, and ensures the session is properly closed after the request
    is completed. Intended to be used as a dependency in FastAPI routes.

    Yields:
        Session: An active SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserLogin(BaseModel):
    """
    UserLogin model for user authentication.

    Attributes:
        correo (EmailStr): The user's email address.
        contrasena (str): The user's password.
    """
    correo: EmailStr
    contrasena: str

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    """
    Handles user login authentication.
    This endpoint verifies the user's credentials and manages account lockout after multiple failed attempts.
    If the user does not exist or the password is incorrect, an appropriate HTTPException is raised.
    After 3 consecutive failed login attempts, the account is temporarily locked for 15 minutes.
    If the account is currently locked, the user is notified.
    On successful login, failed attempts are reset and the lockout is cleared.

    Args:
        user (UserLogin): The login credentials provided by the user.
        db (Session): The database session dependency.

    Returns:
        dict: A message indicating successful login and the user's email.

    Raises:
        HTTPException: If credentials are incorrect, account is locked, or multiple failed attempts occur.
    """
    usuario = db.query(Usuario).filter(Usuario.correo == user.correo).first()
    if not usuario:
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    if usuario.cuenta_bloqueada_hasta and usuario.cuenta_bloqueada_hasta > datetime.utcnow():
        raise HTTPException(status_code=403, detail="Cuenta bloqueada temporalmente. Revisa tu correo.")
    
    if not argon2.verify(user.contrasena, usuario.contrasena_hash):
        usuario.intentos_fallidos += 1
        if usuario.intentos_fallidos >= 3:
            usuario.cuenta_bloqueada_hasta = datetime.utcnow() + timedelta(minutes=15)
            db.commit()
            raise HTTPException(status_code=403, detail="Cuenta bloqueada por múltiples intentos. Revisa tu correo.")
        db.commit()
        raise HTTPException(status_code=400, detail="Correo o contraseña incorrectos")
    
    usuario.intentos_fallidos = 0
    usuario.cuenta_bloqueada_hasta = None
    db.commit()
    
    return {"message": "Inicio de sesión exitoso", "usuario": usuario.correo}
