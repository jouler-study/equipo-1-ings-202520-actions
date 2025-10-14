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

app = FastAPI(title="Registro de Usuarios API", version="1.2")

# Input model for user registration
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)

# Validate password complexity
def validate_password(password: str) -> tuple[bool, str]:
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."
    if not re.search(r"[A-Z]", password):
        return False, "La contraseña debe contener al menos una letra mayúscula."
    if not re.search(r"[0-9]", password):
        return False, "La contraseña debe contener al menos un número."
    if not re.search(r"[!@#$%^&*]", password):
        return False, "La contraseña debe contener al menos un carácter especial (!@#$%^&*)."
    return True, ""

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
        is_valid, message = validate_password(user.password)
        if not is_valid:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=message
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

        # Validate supabase response
        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="El usuario no se pudo crear debido a un error interno."
            )

        # Remove passwords or other sensitive data before returning to the frontend
        created_user = response.data[0]
        if "contrasena_hash" in created_user:
            del created_user["contrasena_hash"]

        return {
            "message": "Usuario creado correctamente.",
            "user": created_user
        }

    except HTTPException as e:
        raise e
    except Exception as e:
        # No handled exceptions
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado en el servidor: {str(e)}"
        )