# password_utils.py
import uuid
import os
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from models import User, EmailLink

def create_password_recovery_link(user: User, db: Session, link_type: str = "recuperacion_password", expiration_hours: int = 1):
    """
    Create a password recovery token and persist it in the DB.

    Args:
        user (User): SQLAlchemy User instance (columns are in Spanish).
        db (Session): SQLAlchemy session.
        link_type (str): type of the link (keeps Spanish default to match DB).
        expiration_hours (int): hours until token expiration.

    Returns:
        (token: str, reset_link: str)
    """
    token = str(uuid.uuid4())
    expires_at = datetime.utcnow() + timedelta(hours=expiration_hours)

    email_link = EmailLink(
        usuario_id=user.usuario_id,
        enlace_url=token,
        tipo=link_type,
        expira_en=expires_at,
        usado=False
    )

    db.add(email_link)
    db.commit()
    db.refresh(email_link)

    # Get frontend URL from environment variable or use default
    frontend_url = os.getenv("FRONTEND_URL", "http://localhost:3000")
    reset_link = f"{frontend_url}/reset-password?token={token}"
    
    return token, reset_link

