from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# Users table
class Usuario(Base):
    __tablename__ = "usuarios" 

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)  # user's full name
    correo = Column(String, unique=True, index=True, nullable=False)  # email address
    contrasena_hash = Column(String, nullable=False)  # hashed password
    intentos_fallidos = Column(Integer, default=0)  # failed login attempts
    cuenta_bloqueada_hasta = Column(DateTime, nullable=True)  # account lock expiration time

    enlaces = relationship("EnlaceCorreo", back_populates="usuario")  # relationship with recovery links


# Email links table (for password recovery or verification)
class EnlaceCorreo(Base):
    __tablename__ = "enlaces_correo"  

    enlace_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)  
    enlace_url = Column(String(500), unique=True, nullable=False)  # unique link/token
    tipo = Column(String(30), nullable=False)  # type of link: "recuperacion_password" or "verificacion_correo"
    expira_en = Column(DateTime, nullable=False)  # expiration date/time
    usado = Column(Boolean, default=False)  # indicates if the link has been used
    fecha_creacion = Column(DateTime, default=datetime.utcnow)  # creation timestamp

    usuario = relationship("Usuario", back_populates="enlaces")  # relationship with user
