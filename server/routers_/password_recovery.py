# password_recovery.py
import os
import smtplib
from email.mime.text import MIMEText
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel, EmailStr
from database import SessionLocal
from models import Usuario
from utils.password_utils import crear_enlace_recuperacion
from passlib.hash import argon2

router = APIRouter(prefix="/password")

# ------------------ #
#   Database Dependency   #
# ------------------ #
def get_db():
    """Creates and closes the database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------- #
#   Pydantic Input Model      #
# --------------------------- #
class ResetPassword(BaseModel):
    nueva_contrasena: str

# ----------------------------- #
#   Password Recovery (POST)    #
# ----------------------------- #
@router.post("/recover/{correo}")
def recover_password(correo: EmailStr, db: Session = Depends(get_db)):
    """
    Starts the password recovery process.

    Args:
        correo (EmailStr): The email address of the user requesting password recovery.
        db (Session): Database session.

    Raises:
        HTTPException: If the user does not exist.

    Returns:
        dict: Message indicating that the recovery email has been sent.
    """
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Generate token and link using the utility function
    token, reset_link = crear_enlace_recuperacion(usuario, db)

    # Create email message
    msg = MIMEText(
        f"Hola {usuario.nombre},\n\n"
        f"✨ Hemos recibido una solicitud para restablecer tu contraseña.\n"
        f"Por favor, haz clic en el siguiente enlace para continuar:\n"
        f"{reset_link}\n\n"
        f"⏰ Este enlace expirará en 1 hora.\n\n"
        f"Si no solicitaste este cambio, puedes ignorar este mensaje.\n\n"
        f"Saludos,\nEl equipo de Soporte de Plaze"
    )
    msg["Subject"] = "🔐 Recuperación de contraseña"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo

    # Send email via Gmail SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el envío del email: {e}")

    return {"message": "Correo de recuperación de contraseña enviado exitosamente"}

# ------------------------ #
#   Reset Password Endpoint #
# ------------------------ #
@router.post("/reset/{token}")
def reset_password(token: str, body: ResetPassword, db: Session = Depends(get_db)):
    """
    Resets a user's password using a valid token.

    Args:
        token (str): Password recovery token.
        body (ResetPassword): Object containing the new password.
        db (Session): Database session.

    Raises:
        HTTPException: If the link is invalid, expired, or already used.

    Returns:
        dict: Success message.
    """
    from models import EnlaceCorreo

    enlace = db.query(EnlaceCorreo).filter(EnlaceCorreo.enlace_url == token).first()

    if not enlace:
        raise HTTPException(status_code=404, detail="Link inválido")
    if enlace.usado:
        raise HTTPException(status_code=400, detail="Link ya fue usado")
    from datetime import datetime
    if enlace.expira_en < datetime.utcnow():
        raise HTTPException(status_code=400, detail="El link ha expirado")

    usuario = db.query(Usuario).filter(Usuario.usuario_id == enlace.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Update the password
    usuario.contrasena = argon2.hash(body.nueva_contrasena)
    enlace.usado = True
    db.commit()

    return {"message": "Contraseña restablecida exitosamente"}
