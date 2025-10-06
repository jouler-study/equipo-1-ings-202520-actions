import uuid
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, EnlaceCorreo
from pydantic import BaseModel, EmailStr
from passlib.hash import argon2
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
import os

router = APIRouter(prefix="/password")

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic model for password reset
class ResetPassword(BaseModel):
    nueva_contrasena: str

# Endpoint to request password recovery
@router.post("/recover/{correo}")
"""
Endpoint to initiate password recovery for a user by email.
Args:
    correo (EmailStr): The email address of the user requesting password recovery.
    db (Session, optional): Database session dependency.
Raises:
    HTTPException: If the user with the provided email is not found (404).
Returns:
    dict: A message indicating that the password recovery email has been sent.
Process:
    - Searches for the user by email in the database.
    - If found, generates a unique recovery token and expiration time (1 hour).
    - Creates a recovery link record associated with the user.
    - Sends an email to the user with a password reset link.
"""
def recover_password(correo: EmailStr, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    token = str(uuid.uuid4())
    expira = datetime.utcnow() + timedelta(hours=1)

    # Create recovery link associated with the user
    enlace = EnlaceCorreo(
        usuario_id=usuario.usuario_id,  # ✅ corrected
        enlace_url=token,
        tipo="recuperacion_password",
        expira_en=expira,
        usado=False
    )
    db.add(enlace)
    db.commit()

    reset_link = f"http://localhost:8000/password/reset/{token}"

    msg = MIMEText(
        f"Hola {usuario.nombre},\n\n"
        f"Haz clic aquí para restablecer tu contraseña:\n{reset_link}\n\n"
        f"Este enlace expira en 1 hora."
    )
    msg["Subject"] = "Recuperación de contraseña"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo

    # Send email with recovery link
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())

    return {"message": "Correo de recuperación enviado"}

# Endpoint to reset password using the token
@router.post("/reset/{token}")
"""
Resets the user's password using a provided token.
This endpoint verifies the validity of the password reset token, checks if it has been used or expired,
and updates the user's password if all checks pass. The token is marked as used after a successful reset.
Args:
    token (str): The password reset token provided in the URL.
    body (ResetPassword): The request body containing the new password.
    db (Session): The database session dependency.
Raises:
    HTTPException: If the token is invalid, already used, expired, or if the user is not found.
Returns:
    dict: A message indicating the password was successfully updated.
"""
def reset_password(token: str, body: ResetPassword, db: Session = Depends(get_db)):
    enlace = db.query(EnlaceCorreo).filter(EnlaceCorreo.enlace_url == token).first()

    if not enlace:
        raise HTTPException(status_code=404, detail="Enlace inválido")
    if enlace.usado:
        raise HTTPException(status_code=400, detail="El enlace ya fue usado")
    if enlace.expira_en < datetime.utcnow():
        raise HTTPException(status_code=400, detail="El enlace ha expirado")

    usuario = db.query(Usuario).filter(Usuario.usuario_id == enlace.usuario_id).first() 
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.contrasena_hash = argon2.hash(body.nueva_contrasena)
    enlace.usado = True
    db.commit()

    return {"message": "Contraseña actualizada correctamente"}
