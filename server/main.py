# main.py
from fastapi import FastAPI
from routers_ import auth, password_recovery
from database import Base, engine
from dotenv import load_dotenv
load_dotenv()

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Prices Plaze API 🛒")

app.include_router(auth.router, tags=["Auth"])
app.include_router(password_recovery.router, tags=["Password Recovery"])

@app.get("/")
def root():
    """
    Root endpoint of the API.

    Returns:
        dict: A JSON response containing a message indicating that the API is running.
    """
    return {"message": "API funcionando 🚀"}

