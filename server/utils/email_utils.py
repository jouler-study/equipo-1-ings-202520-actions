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

    # Compose HTML email
    msg = MIMEText(f"""
    <html>
      <body style="font-family: 'Segoe UI', Arial, sans-serif; background-color: #f7f9fc; margin: 0; padding: 40px;">
        <div style="max-width: 480px; background: #ffffff; margin: auto; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
          <h2 style="color: #d93025; text-align: center;">❌ Cuenta bloqueada temporalmente</h2>
          
          <p style="color: #333;">Hola <b>{nombre_usuario}</b>,</p>
          <p style="color: #333; line-height: 1.5;">
            Tu cuenta ha sido <b>bloqueada temporalmente</b> debido a múltiples intentos fallidos de inicio de sesión.
          </p>
          
          <p style="color: #333; line-height: 1.5;">
            ⏳ Por seguridad, restablece tu contraseña haciendo clic en el siguiente botón:
          </p>

          <div style="text-align: center; margin: 30px 0;">
            <a href="{reset_link}" 
              style="background-color: #1a73e8; color: white; padding: 12px 24px; 
                     border-radius: 8px; text-decoration: none; font-weight: bold; 
                     font-size: 15px; display: inline-block;">
              Restablecer contraseña
            </a>
          </div>

          <p style="color: #555; font-size: 14px;">
            ⚠️ Si no intentaste iniciar sesión, cambia tu contraseña inmediatamente para proteger tu cuenta.
          </p>

          <hr style="border: none; border-top: 1px solid #eee; margin: 25px 0;">
          <p style="color: #777; font-size: 13px; text-align: center;">
            Saludos,<br>
            <b>El equipo de Soporte de Plaze</b>
          </p>
        </div>
      </body>
    </html>
    """, "html")

    msg["Subject"] = "❌ Cuenta bloqueada temporalmente"
    msg["From"] = f"Plaze Soporte <{os.getenv('EMAIL_USER')}>"
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


