from fastapi import FastAPI
from routers import prices

app = FastAPI(title="Market Prices API")

app.include_router(prices.router)

@app.get("/")
def root():
    return {"message": "API funcionando correctamente"}
