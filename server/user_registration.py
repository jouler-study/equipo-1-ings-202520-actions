from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr
from supabase import create_client, Client
from passlib.hash import bcrypt
import re

# Configure Supabase
url = "URL"
key = "KEY"
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
        raise HTTPException(status_code=400, detail="Email already registered")

    # 2. Validate password 
    if not validate_password(user.password):
        raise HTTPException(
            status_code=400, 
            detail="Password must have at least 8 chars, one uppercase, one number and one special char"
        )
    
    # 3. Hash password
    hashed_password = bcrypt.hash(user.password[:72])

    # 4. Insert user
    new_user = {
        "nombre": user.name,
        "correo": user.email,
        "contrasena_hash": hashed_password,
    }

    response = supabase.table("usuarios").insert(new_user).execute()

    # Debugging: show response in console
    print("DEBUG:", response)

    if response.error:
        raise HTTPException(status_code=500, detail=str(response.error))

    return {"message": f"Welcome {user.name} 🎉"}