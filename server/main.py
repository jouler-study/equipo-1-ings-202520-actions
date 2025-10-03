from fastapi import FastAPI
from routers.prices import router as prices_router  # Importamos el router correctamente

app = FastAPI(title="Market Prices API")

# Incluimos el router
app.include_router(prices_router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

