from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal
from models import Usuario
from pydantic import BaseModel, EmailStr
from passlib.hash import argon2
from datetime import datetime, timedelta

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserLogin(BaseModel):
    correo: EmailStr
    contrasena: str

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
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