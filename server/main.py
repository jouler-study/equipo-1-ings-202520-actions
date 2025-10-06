from fastapi import FastAPI
from routers_ import auth, password_recovery
from database import Base, engine

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Prices API")

app.include_router(auth.router, tags=["Auth"])
app.include_router(password_recovery.router, tags=["Password Recovery"])

@app.get("/")
"""
Root endpoint of the API.

Returns:
    dict: A JSON response containing a message indicating that the API is running.
"""
def root():
    return {"message": "API funcionando 🚀"}
