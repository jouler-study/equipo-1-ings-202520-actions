from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal

router = APIRouter(prefix="/prices", tags=["Prices"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/latest/")
def get_latest_price(product_name: str, market_name: str, db: Session = Depends(get_db)):
    query = text("""
        SELECT p.precio_por_kg, p.fecha, pr.nombre AS producto, pl.nombre AS plaza
        FROM precios p
        JOIN productos pr ON pr.producto_id = p.producto_id
        JOIN plazas_mercado pl ON pl.plaza_id = p.plaza_id
        WHERE pr.nombre ILIKE :product_name
          AND pl.nombre ILIKE :market_name
          AND pl.ciudad = 'Medellín'
        ORDER BY p.fecha DESC
        LIMIT 1
    """)

    result = db.execute(query, {
        "product_name": f"%{product_name}%",
        "market_name": f"%{market_name}%"
    }).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para su búsqueda")

    return {
        "product": result.producto,
        "market": result.plaza,
        "price_per_kg": float(result.precio_por_kg),
        "last_update": result.fecha
    }

@router.get("/options/")
def get_options(db: Session = Depends(get_db)):
    """
    Returns the list of products and markets (only Medellín) 
    in a single response for the frontend
    """
    # Get products
    productos_query = text("""
        SELECT producto_id, nombre
        FROM productos
        ORDER BY nombre ASC
    """)
    productos = db.execute(productos_query).fetchall()

    # Get seats only from Medellin
    plazas_query = text("""
        SELECT plaza_id, nombre, ciudad
        FROM plazas_mercado
        WHERE ciudad ILIKE 'Medellín'
        ORDER BY nombre ASC
    """)
    plazas = db.execute(plazas_query).fetchall()

    return {
        "productos": [
            {"id": row.producto_id, "nombre": row.nombre}
            for row in productos
        ],
        "plazas": [
            {"id": row.plaza_id, "nombre": row.nombre, "ciudad": row.ciudad}
            for row in plazas
        ]
    }


@router.get("/productos/")
def listar_productos(db: Session = Depends(get_db)):
    """
    List all available products
    """
    query = text("""
        SELECT producto_id, nombre
        FROM productos
        ORDER BY nombre ASC
    """)
    result = db.execute(query).fetchall()

    return [{"id": row.producto_id, "nombre": row.nombre} for row in result]

@router.get("/plazas/medellin/")
def listar_plazas_medellin(db: Session = Depends(get_db)):
    """
    List all markets in Medellín
    """
    query = text("""
        SELECT plaza_id, nombre, ciudad
        FROM plazas_mercado
        WHERE ciudad = 'Medellín'
        ORDER BY nombre ASC
    """)
    result = db.execute(query).fetchall()

    return [{"id": row.plaza_id, "nombre": row.nombre, "ciudad": row.ciudad} for row in result]
