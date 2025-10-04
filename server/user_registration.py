from fastapi import FastAPI, HTTPException
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

app = FastAPI()

# Input model
class UserRegister(BaseModel):
    name: str
    email: EmailStr
    password: constr(min_length=8)

def validate_password(password: str) -> bool:
    regex = r'^(?=.*[A-Z])(?=.*[0-9])(?=.*[!@#$%^&*]).{8,}$'
    return re.match(regex, password) is not None

@app.post("/registro")
def register_user(user: UserRegister):
    # 1. Check if email already exists
    existing = supabase.table("usuarios").select("*").eq("correo", user.email).execute()
    if existing.data:
        raise HTTPException(status_code=400, detail="Este correo ya ha sido registrado")

    # 2. Validate password 
    if not validate_password(user.password):
        raise HTTPException(
            status_code=400, 
            detail="Las contraseñas deben tener mínimo 8 carácteres, una mayúscula, un número y un carácter especial (!@#$%^&*)."
        )

    # Hash password
    hashed_password = argon2.hash(user.password)

    # Insert user
    response = supabase.table("usuarios").insert({
        "nombre": user.name,
        "correo": user.email,
        "contrasena_hash": hashed_password,
    }).execute()

    if not response.data:
        return {"error": "El usuario no se pudo crear"}

    return {"message": "Usuario creado correctamente", "user": response.data}