# email_utils.py
from sqlalchemy.orm import Session
from database import get_db
from models import User
import smtplib
from email.mime.text import MIMEText
from utils.password_utils import create_password_recovery_link
import os

def send_lock_email(email: str, user_name: str):
    """
    Sends an email notifying that the account has been temporarily locked
    due to multiple failed login attempts, including a recovery link.
    """

    # Create a new database session inside the function
    db: Session = next(get_db())
    user = db.query(User).filter(User.correo == email).first()
    if not user:
        print(f"Usuario {email} no encontrado para correo de bloqueo")
        return

    # Create recovery link
    print("Generando enlace de recuperación...")
    _, reset_link = create_password_recovery_link(user, db)
    print("Link generado:", reset_link)

    # Compose HTML email
    msg = MIMEText(f"""
    <html>
      <body style="font-family: 'Segoe UI', Arial, sans-serif; background-color: #f7f9fc; margin: 0; padding: 40px;">
        <div style="max-width: 480px; background: #ffffff; margin: auto; border-radius: 12px; padding: 30px; box-shadow: 0 4px 10px rgba(0,0,0,0.08);">
          <h2 style="color: #d93025; text-align: center;">❌ Cuenta bloqueada temporalmente</h2>
          
          <p style="color: #333;">Hola <b>{user_name}</b>,</p>
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
    msg["To"] = email

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
            server.sendmail(os.getenv("EMAIL_USER"), email, msg.as_string())
        print(f"Correo de bloqueo enviado a {email}")
    except Exception as e:
        print(f"Error al enviar el correo de bloqueo: {e}")
    finally:
        db.close()



