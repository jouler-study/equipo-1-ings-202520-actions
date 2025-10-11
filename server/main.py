from fastapi import FastAPI
from routers.prices import router as prices_router

app = FastAPI(title="Market Prices API")

# Router included
app.include_router(prices_router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}

