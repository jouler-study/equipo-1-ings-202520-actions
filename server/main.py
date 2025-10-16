# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # CORS middleware for cross-origin requests
from routers_.user_registration import router as user_registration_router
from routers_ import auth, password_recovery
from routers_.prices import router as prices_router
from database import Base, engine
from dotenv import load_dotenv
from routers_.health_routes import router as health_router
from routers_.maintenance_routes import router as maintenance_router

# Load environment variables
load_dotenv()

# Create tables if they do not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Market Prices Plaze API 🛒")

# ========================================
# CORS Configuration
# ========================================
# Enable Cross-Origin Resource Sharing (CORS) to allow frontend requests
# This is required for the React frontend to communicate with the API
# Allowed origins include common development ports (3000, 5173)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",      # Create React App default port
        "http://localhost:5173",      # Vite default port
        "http://127.0.0.1:3000",      # Alternative localhost notation
        "http://127.0.0.1:5173",      # Alternative localhost notation (Vite)
    ],
    allow_credentials=True,           # Allow cookies and authentication headers
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],              # Allow all headers (including Authorization)
)

# Include routers
app.include_router(user_registration_router)
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