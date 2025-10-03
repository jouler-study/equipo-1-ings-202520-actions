from fastapi import FastAPI
from routers.precios import router as prices_router  

app = FastAPI(title="Market Prices API")

# Incluimos el router
app.include_router(prices_router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

