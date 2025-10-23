"""
Price History API module.

This module provides a RESTful endpoint for retrieving and analyzing
the historical price variation of products over a specified period.
It uses the `historial_precios` table to include multiple time points
and provides trend analysis, statistical summaries, and period detection.
"""

from fastapi import APIRouter, HTTPException, Query
from database import SessionLocal
from sqlalchemy import text
from datetime import datetime, timedelta
from typing import List, Dict

# Initialize router for the Price History API
router = APIRouter(
    prefix="/price-history",
    tags=["Price History"]
)


def find_similar_products(db, product_name: str, limit: int = 5) -> List[str]:
    """
    Find products with similar names using partial matching.

    This function performs a case-insensitive search for products whose
    names contain the search term. It's useful for suggesting alternatives
    when an exact match is not found.

    Args:
        db: SQLAlchemy database session for executing queries.
        product_name (str): The product name to search for (supports partial matches).
        limit (int, optional): Maximum number of similar products to return.
            Defaults to 5.

    Returns:
        List[str]: List of product names that match the search pattern.
            Returns empty list if no matches found or if an error occurs.

    Example:
        >>> similar = find_similar_products(db, "tomate", limit=3)
        >>> print(similar)
        ['Tomate', 'Tomate cherry', 'Tomate de árbol']
    """
    try:
        query = text("""
            SELECT DISTINCT prod.nombre
            FROM productos AS prod
            WHERE LOWER(prod.nombre) LIKE LOWER(:search_pattern)
            LIMIT :limit
        """)
        result = db.execute(query, {
            "search_pattern": f"%{product_name}%",
            "limit": limit
        }).fetchall()
        return [row[0] for row in result]
    except Exception:
        return []


def analyze_periods(history: List[Dict]) -> List[Dict]:
    """
    Analyze product price history to detect trend periods.

    This function identifies consecutive periods where prices follow a
    consistent trend (increase, decrease, or stability) and calculates
    the percentage variation for each period.

    Args:
        history (List[Dict]): List of historical price records, each containing:
            - fecha (str): Date in ISO format
            - precio_por_kg (float): Price per kilogram

    Returns:
        List[Dict]: List of detected trend periods, each containing:
            - fecha_inicio (str): Period start date
            - fecha_fin (str): Period end date
            - precio_inicio (float): Initial price
            - precio_fin (float): Final price
            - tendencia (str): Trend type ("Aumento", "Disminución", "Estabilidad")
            - variacion_porcentual (float): Percentage change during the period

    Example:
        >>> history = [
        ...     {"fecha": "2024-01-01", "precio_por_kg": 100},
        ...     {"fecha": "2024-02-01", "precio_por_kg": 110},
        ...     {"fecha": "2024-03-01", "precio_por_kg": 105}
        ... ]
        >>> periods = analyze_periods(history)
        >>> print(periods[0]["tendencia"])
        'Aumento'

    Note:
        A variation greater than 2% is considered an increase, less than -2%
        is a decrease, and between -2% and 2% is considered stability.
    """
    if len(history) < 2:
        return []

    periods = []
    i = 0

    while i < len(history) - 1:
        start = history[i]
        initial_price = start["precio_por_kg"]
        trend = None
        j = i + 1

        while j < len(history):
            current_price = history[j]["precio_por_kg"]
            previous_price = history[j - 1]["precio_por_kg"]
            variation = ((current_price - previous_price) / previous_price) * 100

            if variation > 2:
                new_trend = "Aumento"
            elif variation < -2:
                new_trend = "Disminución"
            else:
                new_trend = "Estabilidad"

            if trend is None:
                trend = new_trend
            elif trend != new_trend:
                break

            j += 1

        end = history[j - 1]
        total_var = ((end["precio_por_kg"] - initial_price) / initial_price) * 100

        periods.append({
            "fecha_inicio": start["fecha"],
            "fecha_fin": end["fecha"],
            "precio_inicio": initial_price,
            "precio_fin": end["precio_por_kg"],
            "tendencia": trend,
            "variacion_porcentual": round(total_var, 2)
        })

        i = j

    return periods


@router.get("/{product_name}")
def get_price_history(
    product_name: str,
    months: int = Query(
        12,
        ge=1,
        le=120,
        description="Number of months to query (min: 1, max: 120, default: 12)"
    )
) -> Dict:
    """
    Retrieve and analyze the historical price variation of a product.

    This endpoint queries the historial_precios table to fetch complete
    price history for a specified product over a given time period. It
    provides statistical analysis, trend detection, and detailed historical data.

    Args:
        product_name (str): Name of the product to query. Supports hyphens
            and underscores which are normalized to spaces.
        months (int, optional): Number of months to look back in history.
            Must be between 1 and 120. Defaults to 12 months.

    Returns:
        Dict: A comprehensive price history analysis containing:
            - producto (str): Normalized product name
            - periodo_meses (int): Number of months analyzed
            - fecha_inicio (str): First date in the dataset
            - fecha_fin (str): Last date in the dataset
            - tendencia_general (str): Overall trend classification
            - estadisticas (dict): Statistical summary including initial, final,
              average, max, min prices and percentage change
            - periodos (List[Dict]): Detected trend periods with details
            - historial (List[Dict]): Complete chronological price records

    Raises:
        HTTPException: 400 if months parameter is invalid (not between 1 and 120).
        HTTPException: 404 if no data found for the product.
            If similar products exist, they are suggested in the error message.

    Example:
        >>> response = get_price_history("tomate", months=6)
        >>> print(response["tendencia_general"])
        'Aumento'
        >>> print(response["estadisticas"]["precio_promedio"])
        45.32

    Note:
        - Product names are normalized by removing spaces and hyphens
          for flexible matching
        - Prices are retrieved from the historial_precios table
        - Trends are classified as "Aumento" (>5%), "Disminución" (<-5%),
          or "Estabilidad" (between -5% and 5%)
        - Valid months range: 1-120 (1 month to 10 years)
    """
    db = SessionLocal()
    try:
        # Validate months parameter
        if months < 1 or months > 120:
            raise HTTPException(
                status_code=400,
                detail="El parámetro 'months' debe estar entre 1 y 120. "
                       f"Valor recibido: {months}"
            )

        product_name_normalized = product_name.replace("-", " ").replace("_", " ").strip()
        start_date = datetime.utcnow() - timedelta(days=30 * months)

        # ✅ Query now uses historial_precios instead of precios
        query = text("""
            SELECT 
                hp.fecha_precio AS fecha,
                hp.precio_historico AS precio_por_kg
            FROM historial_precios AS hp
            JOIN productos AS prod ON hp.producto_id = prod.producto_id
            WHERE LOWER(REPLACE(REPLACE(prod.nombre, ' ', ''), '-', '')) = 
                  LOWER(REPLACE(REPLACE(:product_name, ' ', ''), '-', ''))
              AND hp.fecha_precio >= :start_date
            ORDER BY hp.fecha_precio ASC
        """)

        result = db.execute(query, {
            "product_name": product_name_normalized,
            "start_date": start_date
        }).fetchall()

        # Handle no data found
        if not result:
            similar = find_similar_products(db, product_name_normalized)
            if similar:
                raise HTTPException(
                    status_code=404,
                    detail=f"No se encontraron datos para '{product_name}'. "
                           f"¿Quisiste decir: {', '.join(similar)}?"
                )
            raise HTTPException(
                status_code=404,
                detail=f"No se encontraron datos históricos para '{product_name}' "
                       f"en los últimos {months} meses."
            )

        # Build structured history
        history = [{
            "fecha": (r[0].isoformat() if hasattr(r[0], "isoformat") else str(r[0])),
            "precio_por_kg": float(r[1])
        } for r in result]

        # Basic statistics
        initial_price = history[0]["precio_por_kg"]
        final_price = history[-1]["precio_por_kg"]
        percent_change = ((final_price - initial_price) / initial_price) * 100

        if percent_change > 5:
            trend_general = "Aumento"
        elif percent_change < -5:
            trend_general = "Disminución"
        else:
            trend_general = "Estabilidad"

        prices = [p["precio_por_kg"] for p in history]
        avg_price = sum(prices) / len(prices)

        # Detect specific trend periods
        periods = analyze_periods(history)

        return {
            "producto": product_name_normalized,
            "periodo_meses": months,
            "fecha_inicio": history[0]["fecha"],
            "fecha_fin": history[-1]["fecha"],
            "tendencia_general": trend_general,
            "estadisticas": {
                "precio_inicial": initial_price,
                "precio_final": final_price,
                "precio_promedio": round(avg_price, 2),
                "precio_maximo": max(prices),
                "precio_minimo": min(prices),
                "variacion_porcentual": round(percent_change, 2),
                "total_registros": len(history)
            },
            "periodos": periods,
            "historial": history
        }

    finally:
        db.close()