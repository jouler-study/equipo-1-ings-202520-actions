import uuid
import os
import smtplib
from email.mime.text import MIMEText
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario, EnlaceCorreo
from pydantic import BaseModel, EmailStr
from passlib.hash import argon2

router = APIRouter(prefix="/password")


# ------------------ #
#   Dependencia DB   #
# ------------------ #
def get_db():
    """Crea y cierra la sesión con la base de datos."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------------- #
#   Modelo Pydantic de input  #
# --------------------------- #
class ResetPassword(BaseModel):
    nueva_contrasena: str


# ----------------------------- #
#   Recuperar contraseña (POST) #
# ----------------------------- #
@router.post("/recover/{correo}")
def recover_password(correo: EmailStr, db: Session = Depends(get_db)):
    """
    Inicia el proceso de recuperación de contraseña.

    Args:
        correo (EmailStr): Correo del usuario que solicita recuperar la contraseña.
        db (Session): Sesión de la base de datos.

    Raises:
        HTTPException: Si el usuario no existe.

    Returns:
        dict: Mensaje indicando que el correo fue enviado.
    """
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    # Generar token único con expiración
    token = str(uuid.uuid4())
    expira = datetime.utcnow() + timedelta(hours=1)

    # Crear enlace de recuperación
    enlace = EnlaceCorreo(
        usuario_id=usuario.usuario_id,
        enlace_url=token,
        tipo="recuperacion_password",
        expira_en=expira,
        usado=False
    )
    db.add(enlace)
    db.commit()

    # 🔗 Enlace temporal (actualízalo cuando tengas el front)
    reset_link = f"http://localhost:8000/password/reset/{token}"

    # Crear correo
    msg = MIMEText(
        f"Hola {usuario.nombre},\n\n"
        f"Haz clic en el siguiente enlace para restablecer tu contraseña:\n"
        f"{reset_link}\n\n"
        f"Este enlace expirará en 1 hora.\n\n"
        f"Si no solicitaste este cambio, ignora este mensaje."
    )
    msg["Subject"] = "Recuperación de contraseña"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo

    # Enviar correo
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al enviar el correo: {e}")

    return {"message": "Correo de recuperación enviado"}


# ------------------------ #
#   Restablecer contraseña #
# ------------------------ #
@router.post("/reset/{token}")
def reset_password(token: str, body: ResetPassword, db: Session = Depends(get_db)):
    """
    Restablece la contraseña de un usuario usando un token válido.

    Args:
        token (str): Token de recuperación.
        body (ResetPassword): Nueva contraseña.
        db (Session): Sesión de la base de datos.

    Raises:
        HTTPException: Si el enlace es inválido, usado o expirado.

    Returns:
        dict: Mensaje de éxito.
    """
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

    # Actualizar contraseña
    usuario.contrasena_hash = argon2.hash(body.nueva_contrasena)
    enlace.usado = True
    db.commit()

    return {"message": "Contraseña actualizada correctamente"}
