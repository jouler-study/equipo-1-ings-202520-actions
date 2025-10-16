# prices.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db

router = APIRouter(prefix="/prices", tags=["Prices"])

# --- Endpoint 1: Get the latest price ---
@router.get("/latest/")
def get_latest_price(product_name: str, market_name: str, db: Session = Depends(get_db)):
    """
    Retrieve the latest price for a given product and market in Medellín.
    Handles misspellings or similar names by suggesting close matches.
    """
    # First, try to find an exact or close match
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

    # If not found, suggest possible similar product names
    if not result:
        suggestion_query = text("""
            SELECT nombre 
            FROM productos
            WHERE nombre ILIKE :similar
            ORDER BY nombre ASC
            LIMIT 5
        """)
        suggestions = db.execute(suggestion_query, {"similar": f"%{product_name[:3]}%"}).fetchall()
        suggested_names = [s.nombre for s in suggestions]

        if suggested_names:
            raise HTTPException(
                status_code=404,
                detail={
                    "message": "No se encontraron resultados exactos. ¿Quizás quiso decir uno de estos?",
                    "suggestions": suggested_names
                }
            )
        else:
            raise HTTPException(
                status_code=404,
                detail="No se encontraron resultados para su búsqueda."
            )

    return {
        "producto": result.producto,
        "plaza": result.plaza,
        "precio_por_kg": float(result.precio_por_kg),
        "ultima_actualizacion": result.fecha,
        "mensaje": "Consulta realizada exitosamente."
    }

# --- Endpoint 2: Get all available options ---
@router.get("/options/")
def get_options(db: Session = Depends(get_db)):
    """
    Return available products and markets (only Medellín) for the frontend.
    """
    productos_query = text("""
        SELECT producto_id, nombre
        FROM productos
        ORDER BY nombre ASC
    """)
    productos = db.execute(productos_query).fetchall()

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
        ],
        "mensaje": "Opciones disponibles obtenidas correctamente."
    }

# --- Endpoint 3: List all products ---
@router.get("/products/")
def list_products(db: Session = Depends(get_db)):
    """
    List all available products.
    """
    query = text("""
        SELECT producto_id, nombre
        FROM productos
        ORDER BY nombre ASC
    """)
    result = db.execute(query).fetchall()

    return {
        "productos": [{"id": row.producto_id, "nombre": row.nombre} for row in result],
        "mensaje": "Lista de productos obtenida exitosamente."
    }

# --- Endpoint 4: List all markets in Medellín ---
@router.get("/markets/medellin/")
def list_medellin_markets(db: Session = Depends(get_db)):
    """
    List all markets in Medellín.
    """
    query = text("""
        SELECT plaza_id, nombre, ciudad
        FROM plazas_mercado
        WHERE ciudad = 'Medellín'
        ORDER BY nombre ASC
    """)
    result = db.execute(query).fetchall()

    return {
        "plazas": [{"id": row.plaza_id, "nombre": row.nombre, "ciudad": row.ciudad} for row in result],
        "mensaje": "Lista de plazas de Medellín obtenida exitosamente."
    }
