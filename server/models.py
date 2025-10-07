from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Users table
class Usuario(Base):
    """
    Represents a user account in the system.
    Attributes:
        usuario_id (int): Primary key identifier for the user.
        nombre (str): Full name of the user.
        correo (str): Unique email address of the user.
        contrasena_hash (str): Hashed password for authentication.
        intentos_fallidos (int): Number of consecutive failed login attempts.
        cuenta_bloqueada_hasta (datetime): Timestamp until which the account is locked due to failed attempts.
        enlaces (List[EnlaceCorreo]): Relationship to password recovery links associated with the user.
    """
    __tablename__ = "usuarios" 

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)  # user's full name
    correo = Column(String, unique=True, index=True, nullable=False)  # email address
    contrasena_hash = Column(String, nullable=False)  # hashed password
    rol = Column(String, default="usuario")  # user role: "usuario" or "admin"
    intentos_fallidos = Column(Integer, default=0)  # failed login attempts
    cuenta_bloqueada_hasta = Column(DateTime, nullable=True)  # account lock expiration time

    enlaces = relationship("EnlaceCorreo", back_populates="usuario")  # relationship with recovery links


# Email links table (for password recovery or verification)
class EnlaceCorreo(Base):
    """
    Represents an email link entity used for actions such as password recovery or email verification.
    Attributes:
        enlace_id (int): Primary key identifier for the email link.
        usuario_id (int): Foreign key referencing the associated user.
        enlace_url (str): Unique URL or token for the link.
        tipo (str): Type of link, e.g., "recuperacion_password" or "verificacion_correo".
        expira_en (datetime): Expiration date and time of the link.
        usado (bool): Indicates whether the link has been used.
        fecha_creacion (datetime): Timestamp of when the link was created.
        usuario (Usuario): Relationship to the associated user.
    """
    __tablename__ = "enlaces_correo"  

    enlace_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)  
    enlace_url = Column(String(500), unique=True, nullable=False)  # unique link/token
    tipo = Column(String(30), nullable=False)  # type of link: "recuperacion_password" or "verificacion_correo"
    expira_en = Column(DateTime, nullable=False)  # expiration date/time
    usado = Column(Boolean, default=False)  # indicates if the link has been used
    fecha_creacion = Column(DateTime, default=datetime.utcnow)  # creation timestamp

    usuario = relationship("Usuario", back_populates="enlaces")  # relationship with user
