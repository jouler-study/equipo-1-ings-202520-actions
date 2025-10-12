# models.py
from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime

# ==========================
# 👤 User-related models
# ==========================
class User(Base):
    """
    ORM model for users table.
    Column names remain in Spanish to match the DB schema.
    """
    __tablename__ = "usuarios"

    usuario_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    correo = Column(String, unique=True, index=True, nullable=False)
    contrasena_hash = Column(String, nullable=False)
    rol = Column(String, default="usuario")  # e.g. "usuario" or "admin"
    intentos_fallidos = Column(Integer, default=0)
    cuenta_bloqueada_hasta = Column(DateTime, nullable=True)

    enlaces = relationship("EmailLink", back_populates="user")


class EmailLink(Base):
    """
    ORM model for email links (password recovery / email verification).
    Column names remain in Spanish to match the DB schema.
    """
    __tablename__ = "enlaces_correo"

    enlace_id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey("usuarios.usuario_id"), nullable=False)
    enlace_url = Column(String(500), unique=True, nullable=False)
    tipo = Column(String(30), nullable=False)
    expira_en = Column(DateTime, nullable=False)
    usado = Column(Boolean, default=False)
    fecha_creacion = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="enlaces")


# ==========================
# 🏪 Market-related models
# ==========================
class Price(Base):
    __tablename__ = "precios"

    price_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("productos.producto_id"), nullable=False)
    market_id = Column(Integer, ForeignKey("plazas_mercado.plaza_id"), nullable=False)
    price_per_kg = Column(DECIMAL(10, 2), nullable=False)
    date = Column(Date, nullable=False)

    producto = relationship("Producto", back_populates="precios")
    plaza = relationship("PlazaMercado", back_populates="precios")


class PlazaMercado(Base):
    __tablename__ = "plazas_mercado"

    plaza_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    ciudad = Column(String, nullable=False)

    precios = relationship("Price", back_populates="plaza")


class Producto(Base):
    __tablename__ = "productos"

    producto_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, unique=True, nullable=False)

    precios = relationship("Price", back_populates="producto")
