# emails_utils.py
import os
import smtplib
from email.mime.text import MIMEText
from utils.password_utils import crear_enlace_recuperacion
from sqlalchemy.orm import Session
from models import Usuario

def enviar_correo_bloqueo(correo: str, nombre_usuario: str, db: Session):
    """
    Sends an email notifying that the account has been temporarily blocked
    due to multiple failed login attempts, including a recovery link.
    """
    # Search for user in the database
    usuario = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not usuario:
        print(f"Usuario {correo} no encontrado para correo de bloqueo")
        return

    # Create recovery link using the utility function
    _, reset_link = crear_enlace_recuperacion(usuario, db)

    # Create email message
    msg = MIMEText(
        f"🔒 Hola {nombre_usuario},\n\n"
        f"Tu cuenta ha sido bloqueada temporalmente por múltiples intentos fallidos de inicio de sesión.\n"
        f"⏳ Por seguridad, debes restablecer tu contraseña usando el siguiente enlace:\n"
        f"{reset_link}\n\n"
        f"⚠️ Si no realizaste estos intentos, te recomendamos cambiar tu contraseña lo antes posible.\n\n"
        f"Saludos,\nEl equipo de soporte de Plaze"
    )
    msg["Subject"] = "❌ Cuenta bloqueada temporalmente"
    msg["From"] = os.getenv("EMAIL_USER")
    msg["To"] = correo
    # Send email via Gmail SMTP
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), correo, msg.as_string())
    except Exception as e:
        print(f"Error enviando correo de bloqueo: {e}")

