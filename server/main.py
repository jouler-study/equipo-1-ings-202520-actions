# This main is temporary for testing this availability feature and will be merged with main.py when merging.
from fastapi import FastAPI
from routes.health_routes import router as health_router

app = FastAPI(title="API - Predicción de precios (Pruebas de disponibilidad local)")

# Include the health check router
app.include_router(health_router)

@app.get("/")
def root():
    return {"message": "API de pruebas funcionando"}