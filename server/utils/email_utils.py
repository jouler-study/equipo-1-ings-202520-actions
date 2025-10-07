# emails_utils.py
from sqlalchemy.orm import Session
from database import get_db
from models import Usuario
import smtplib
from email.mime.text import MIMEText
from utils.password_utils import crear_enlace_recuperacion
import os

def enviar_correo_bloqueo(correo: str, nombre_usuario: str):
    """
    Sends an email notifying that the account has been temporarily blocked
    due to multiple failed login attempts, including a recovery link.
    """

    # Create a new DB session inside the function
    db: Session = next(get_db())
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        print(f"Usuario {correo} no encontrado para correo de bloqueo")
        return

    # Create recovery link
    print("Generando enlace de recuperación...")
    _, reset_link = crear_enlace_recuperacion(usuario, db)
    print("Link generado:", reset_link)

    # Compose email
    msg = MIMEText(
        f"🔒 Hola {nombre_usuario},\n\n"
        f"Tu cuenta ha sido bloqueada temporalmente debido a múltiples intentos fallidos de inicio de sesión.\n"
        f"⏳ Por seguridad, restablece tu contraseña usando este enlace:\n{reset_link}\n\n"
        f"⚠️ Si no intentaste iniciar sesión, cambia tu contraseña inmediatamente.\n\n"
        f"Saludos,\nEquipo de Soporte"
    )
    msg["Subject"] = "❌ Cuenta bloqueada temporalmente"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())
        print(f"Lock email sent to {correo}")
    except Exception as e:
        print(f"Error sending lock email: {e}")
    finally:
        db.close()

