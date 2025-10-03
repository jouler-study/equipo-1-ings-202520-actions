from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
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
    query = """
        SELECT p.precio_por_kg, p.fecha, pr.nombre AS producto, pl.nombre AS plaza
        FROM precios p
        JOIN productos pr ON pr.producto_id = p.producto_id
        JOIN plazas_mercado pl ON pl.plaza_id = p.plaza_id
        WHERE pr.nombre ILIKE %s AND pl.nombre ILIKE %s AND pl.ciudad='Medellín'
        ORDER BY p.fecha DESC
        LIMIT 1
    """
    result = db.execute(query, (product_name, market_name)).fetchone()

    if not result:
        raise HTTPException(status_code=404, detail="No se encontraron resultados para su búsqueda")

    return {
        "product": result.producto,
        "market": result.plaza,
        "price_per_kg": float(result.precio_por_kg),
        "last_update": result.fecha
    }

