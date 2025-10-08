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
import re

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

    # Create HTML email message (table-based for consistent layout)
    msg = MIMEText(f"""
<html>
  <body style="margin: 0; padding: 0; background-color: #f4f6f8;">
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
      <tr>
        <td align="center" style="padding: 40px 0;">
          <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="480" style="background-color: #ffffff; border-radius: 12px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
            <tr>
              <td style="padding: 30px 40px; font-family: Arial, sans-serif; color: #333;">
                
                <h2 style="color: #1a73e8; text-align: center; margin-top: 0;">
                  🔐 Recuperación de contraseña
                </h2>
                
                <p>Hola <b>{usuario.nombre}</b>,</p>

                <p style="line-height: 1.6;">
                  Hemos recibido una solicitud para restablecer tu contraseña.<br>
                  Por favor, haz clic en el botón de abajo para continuar:
                </p>

                <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin: 30px auto;">
                  <tr>
                    <td align="center" bgcolor="#1a73e8" style="border-radius: 8px;">
                      <a href="{reset_link}" target="_blank" 
                        style="display: inline-block; padding: 12px 24px; font-size: 16px; 
                               font-weight: bold; color: #ffffff; text-decoration: none; 
                               border-radius: 8px;">
                        Restablecer contraseña
                      </a>
                    </td>
                  </tr>
                </table>

                <p style="color: #555; font-size: 14px;">
                  ⏰ Este enlace expirará en <b>1 hora</b>.<br>
                  Si no solicitaste este cambio, puedes ignorar este mensaje.
                </p>

                <hr style="border: none; border-top: 1px solid #eee; margin: 25px 0;">

                <p style="color: #777; font-size: 13px; text-align: center;">
                  Saludos,<br>
                  <b>El equipo de Soporte de Plaze</b>
                </p>

              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
  </body>
</html>
""", "html")

    msg["Subject"] = "🔐 Recuperación de contraseña"
    msg["From"] = f"Plaze Soporte <{os.getenv('EMAIL_USER')}>"
    msg["To"] = correo

    # Send email via Gmail SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el envío del email: {e}")

    return {"message": "Correo de recuperación de contraseña enviado exitosamente"}


import re
from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from passlib.hash import argon2
from models import Usuario, EnlaceCorreo
from datetime import datetime

# ------------------------ #
#   Validación de contraseña
# ------------------------ #
def validate_password(password: str) -> bool:
    regex = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$'
    return re.match(regex, password) is not None

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
        HTTPException: If the link is invalid, expired, already used, or password invalid.

    Returns:
        dict: Success message.
    """
    enlace = db.query(EnlaceCorreo).filter(EnlaceCorreo.enlace_url == token).first()

    if not enlace:
        raise HTTPException(status_code=404, detail="Link inválido")
    if enlace.usado:
        raise HTTPException(status_code=400, detail="Link ya fue usado")
    if enlace.expira_en < datetime.utcnow():
        raise HTTPException(status_code=400, detail="El link ha expirado")

    usuario = db.query(Usuario).filter(Usuario.usuario_id == enlace.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Validar la nueva contraseña
    if not validate_password(body.nueva_contrasena):
        raise HTTPException(
            status_code=400,
            detail="La contraseña debe tener al menos 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*)"
        )

    # Actualizar la contraseña
    usuario.contrasena_hash = argon2.hash(body.nueva_contrasena)
    enlace.usado = True
    db.commit()
    db.refresh(usuario)

    return {"message": "Contraseña restablecida exitosamente"}

