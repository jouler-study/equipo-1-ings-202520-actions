from fastapi import APIRouter, HTTPException, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, constr
from supabase import create_client, Client
from passlib.hash import argon2
from dotenv import load_dotenv
import os
import re

# Router instance
router = APIRouter(prefix="/registro", tags=["User Registration"])

# Load environment variables from /server/.env
env_path = os.path.join(os.path.dirname(__file__), "../.env")
load_dotenv(dotenv_path=env_path)

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

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

# Register user endpoint
@router.post("/")
def register_user(user: UserRegister):
    try:
        existing = supabase.table("usuarios").select("*").eq("correo", user.email).execute()
        if existing.data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este correo ya ha sido registrado."
            )

        is_valid, message = validate_password(user.password)
        if not is_valid:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=message)

        hashed_password = argon2.hash(user.password)

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

        if not response.data:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="El usuario no se pudo crear debido a un error interno."
            )

        created_user = response.data[0]
        created_user.pop("contrasena_hash", None)

        return {"message": "Usuario creado correctamente.", "user": created_user}

    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inesperado en el servidor: {str(e)}"
        )