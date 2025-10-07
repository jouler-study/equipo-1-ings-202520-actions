# password_utils.py
import uuid
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import Usuario, EnlaceCorreo

def crear_enlace_recuperacion(usuario: Usuario, db: Session, tipo="recuperacion_password", expiracion_horas=1):
    """
    Creates a password recovery token and saves it in the database.
    Returns the generated token and the reset URL.
    """
    token = str(uuid.uuid4())
    expira = datetime.utcnow() + timedelta(hours=expiracion_horas)

    enlace = EnlaceCorreo(
        usuario_id=usuario.usuario_id,
        enlace_url=token,
        tipo=tipo,
        expira_en=expira,
        usado=False
    )
    db.add(enlace)
    db.commit()

    reset_link = f"http://localhost:8000/password/reset/{token}"
    return token, reset_link
