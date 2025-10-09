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
load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

app = FastAPI(title="Registro de Usuarios API", version="1.0")

# Input model for user registration
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)

# Validate password with custom rules
def validate_password(password: str) -> bool:
    regex = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$'
    return re.match(regex, password) is not None

# Error handler to translate validation errors to Spanish
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    translated_errors = []
    for error in exc.errors():
        msg = error["msg"]

        # Translate common pydantic error messages to Spanish
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

# Register user endpoint
@app.post("/registro")
def register_user(user: UserRegister):
    # 1. Validate if email already exists
    existing = supabase.table("usuarios").select("*").eq("correo", user.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Este correo ya ha sido registrado")

    # 2. Validate password complexity
    if not validate_password(user.password):
        raise HTTPException(
            status_code=400, 
            detail="La contraseña debe tener mínimo 8 caracteres, una mayúscula, un número y un carácter especial (!@#$%^&*)."
        )

    # 3. Encrypt password
    hashed_password = argon2.hash(user.password)

    # 4. Insert the new user into the database
    response = supabase.table("usuarios").insert({
        "nombre": user.name,
        "correo": user.email,
        "contrasena_hash": hashed_password,
    }).execute()

    if not response.data:
        return {"error": "El usuario no se pudo crear"}

    return {"message": "Usuario creado correctamente", "user": response.data}