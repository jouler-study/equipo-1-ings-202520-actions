# 🧩 User Registration API – FastAPI + Supabase

This module implements a **user registration system** using **FastAPI**, **Supabase**, and **Argon2** for secure password hashing.

---

## 🚀 Features

- **User registration** via `/registro` endpoint.  
- **Detailed password validation** with specific feedback messages.  
- **Email format and duplication validation**.  
- **Secure password hashing** using Argon2 (never returned to the client).  
- **Supabase integration** for PostgreSQL database operations.  
- **Proper HTTP error handling** with `HTTPException`.  
- **Environment variables (.env)** loaded from the `/server` directory.  

---

## 🧰 Requirements

### Python version
- Python **3.11+**
- Access to an account and project in **Supabase**
- Environment variables configured correctly

### Dependencies
Make sure you have **pip** installed, then run:

```PowerShell
pip install fastapi "uvicorn[standard]" supabase passlib[argon2] python-dotenv "pydantic[email]"
```

```PowerShell
If you encounter errors with bcrypt, try:
> pip install --upgrade passlib bcrypt
```

If you encounter errors with uvicorn:
> WARNING: The script uvicorn.exe is installed in 'C:\Users\<your_user>\AppData\Roaming\Python\Python313\Scripts' which is not on PATH.

Add that path to your PATH or use the following alternative command to run the server:
```PowerShell
> python -m uvicorn server.user_registration:app --reload
```

### ⚙️ Environment Setup
In the server directory, create a .env file with the following content:

>  SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_API_KEY

⚠️ Ensure that the URL begins with https://, or the following error will appear:
> supabase._sync.client.SupabaseException: Invalid URL

### 🧩 Project Structure
EQUIPO-1-INGS-202520/
│
├── client/
├── doc/
├── server/
│   └── user_registration.py
├── .env
└── .gitignore

### ▶️ Running the Server
From the root directory of your project, run:
#### Option 1 (if uvicorn is in PATH)
```PowerShell
uvicorn server.user_registration:app --reload
```

#### Option 2 (recommended for Windows)
```PowerShell
python -m uvicorn server.user_registration:app --reload
```

Then open your browser or API tool (like Postman) and go to:
> http://127.0.0.1:8000/docs

You will find the interactive Swagger UI where you can test the /registro endpoint.

### Example Request
Endpoint: POST /registro
Body:
> {
  "name": "Molly",
  "email": "molly@example.com",
  "password": "UnaBuenaContraseña*1"
}

Possible Responses:
* 200 OK → User created successfully.

* 400 Bad Request → Invalid password or email already registered.

* 422 Unprocessable Entity → Validation error in one or more fields.

* 503 Service Unavailable → Database connection issue.

* 500 Internal Server Error → Unexpected server error.

### Security & Improvements
* Passwords are hashed with Argon2 before storage.

* The password hash is never returned to the frontend in any response.

* The function validate_password() now provides detailed user feedback when the password fails validation

### Notes
* Passwords must contain at least 8 characters, including one uppercase, one number, and one special character (!@#$%^&*).

* All user data is stored in the Supabase table usuarios.

* Update .env credentials if Supabase project details change.