from fastapi import FastAPI
from routers_ import auth, password_recovery
from database import Base, engine

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Prices API")

app.include_router(auth.router, tags=["Auth"])
app.include_router(password_recovery.router, tags=["Password Recovery"])

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}
