# main.py
from fastapi import FastAPI
from routers_ import auth, password_recovery
from routers.prices import router as prices_router
from database import Base, engine
from dotenv import load_dotenv
from routes.health_routes import router as health_router
from routes.maintenance_routes import router as maintenance_router

# Load environment variables
load_dotenv()

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Prices Plaze API 🛒")

# Include routers
app.include_router(auth.router, tags=["Auth"])
app.include_router(password_recovery.router, tags=["Password Recovery"])
app.include_router(prices_router, tags=["Prices"])
app.include_router(health_router)
app.include_router(maintenance_router)

@app.get("/")
def root():
    """
    Root endpoint of the API.

    Returns:
        dict: A JSON response containing a message indicating that the API is running.
    """
    return {"message": "API funcionando 🚀"}