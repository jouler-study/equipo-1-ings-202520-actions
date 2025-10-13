from fastapi import FastAPI, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, constr
from supabase import create_client, Client
from passlib.hash import argon2
from dotenv import load_dotenv
import os
import re

# Load environment variables
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=env_path)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI(title="Registro de Usuarios API", version="1.1")

# Input model for user registration
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)

# Validate password complexity
def validate_password(password: str) -> bool:
    regex = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$'
    return re.match(regex, password) is not None

# Error handler for validation errors with Spanish translations
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    translated_errors = []
    for error in exc.errors():
        msg = error["msg"]

        if "field required" in msg:
            msg = "Este campo es obligatorio."
        elif "at least" in msg:
            msg = "La contraseña debe tener al menos 8 caracteres."
        elif "valid email address" in msg:
            msg = "El correo electrónico no es válido."
        elif "string type expected" in msg:
            msg = "Este campo debe ser una cadena de texto."
        elif "none is not an allowed value" in msg:
            msg = "El valor no puede ser nulo."

        translated_errors.append({
            "campo": error["loc"][-1],
            "mensaje": msg
        })

    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"errores": translated_errors}
    )

# User registration endpoint
@app.post("/registro")
def register_user(user: UserRegister):
    try:
        # Validate email uniqueness
        existing = supabase.table("usuarios").select("*").eq("correo", user.email).execute()
        if existing.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este correo ya ha sido registrado."
            )

        # Validate password complexity
        if not validate_password(user.password):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*)."
            )

        # Encrypt password
        hashed_password = argon2.hash(user.password)

        # Insert user into database
        try:
            response = supabase.table("usuarios").insert({
                "nombre": user.name,
                "correo": user.email,
                "contrasena_hash": hashed_password,
            }).execute()
        except Exception:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Error al conectarse con la base de datos. Inténtalo nuevamente más tarde."
            )

        #  Validate insertion response
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="El usuario no se pudo crear debido a un error interno."
            )

        # Remove passwords or other sensitive data before returning to the frontend
        created_user = response.data[0]  # Supabase returns a list of inserted rows
        if "contrasena_hash" in created_user:
            del created_user["contrasena_hash"]

        return {
            "message": "Usuario creado correctamente.",
            "user": created_user
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        # No handle unexpected errors
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado en el servidor: {str(e)}"
        )