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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class ResetPassword(BaseModel):
    nueva_contrasena: str

@router.post("/recover/{correo}")
def recover_password(correo: EmailStr, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    token = str(uuid.uuid4())
    expira = datetime.utcnow() + timedelta(hours=1)

    enlace = EnlaceCorreo(
        usuario_id=usuario.id,
        enlace_url=token,
        tipo="recuperacion_password",
        expira_en=expira,
        usado=False
    )
    db.add(enlace)
    db.commit()

    reset_link = f"http://localhost:8000/password/reset/{token}"

    msg = MIMEText(f"Hola {usuario.nombre},\n\nHaz clic aquí para restablecer tu contraseña:\n{reset_link}\n\nEste enlace expira en 1 hora.")
    msg["Subject"] = "Recuperación de contraseña"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())

    return {"message": "Correo de recuperación enviado"}

@router.post("/reset/{token}")
def reset_password(token: str, body: ResetPassword, db: Session = Depends(get_db)):
    enlace = db.query(EnlaceCorreo).filter(EnlaceCorreo.enlace_url == token).first()

    if not enlace:
        raise HTTPException(status_code=404, detail="Enlace inválido")
    if enlace.usado:
        raise HTTPException(status_code=400, detail="El enlace ya fue usado")
    if enlace.expira_en < datetime.utcnow():
        raise HTTPException(status_code=400, detail="El enlace ha expirado")

    usuario = db.query(Usuario).filter(Usuario.id == enlace.usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    usuario.contrasena_hash = argon2.hash(body.nueva_contrasena)
    enlace.usado = True
    db.commit()

    return {"message": "Contraseña actualizada correctamente"}
