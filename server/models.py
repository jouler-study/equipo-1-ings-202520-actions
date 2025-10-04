from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Price(Base):
    __tablename__ = "precios"  

    price_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("productos.producto_id"), nullable=False)
    market_id = Column(Integer, ForeignKey("plazas_mercado.plaza_id"), nullable=False)
    price_per_kg = Column(DECIMAL(10,2), nullable=False)
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
