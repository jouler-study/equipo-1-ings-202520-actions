# 🧩 User Registration API – FastAPI + Supabase

This module implements a **user registration system** using **FastAPI**, **Supabase**, and **Argon2** for secure password hashing.

---

## 🚀 Features

- **User registration** via `/registro` endpoint.  
- **Validation** for email and password strength.  
- **Secure password hashing** with Argon2.  
- **Supabase integration** for PostgreSQL database operations.  
- **Environment variables (.env)** for sensitive credentials.  

---

## 🧰 Requirements

### Python version
- Python **3.10+**

### Dependencies
Make sure you have **pip** installed, then run:

```bash
pip install fastapi uvicorn supabase passlib[bcrypt] python-dotenv
```

> 💡 If you encounter errors with `bcrypt`, try:
```bash
pip install --upgrade passlib bcrypt
```

---

## ⚙️ Environment Setup

In the root of your project (same level as `server/`), create a file named `.env` with:

```bash
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_API_KEY
```

> ⚠️ Never push your `.env` file to GitHub — make sure it’s listed in `.gitignore`.

Example `.gitignore`:
```
__pycache__/
*.pyc
.env
```

---

## 🧩 Project Structure

```
EQUIPO-1-INGS-202520/
│
├── client/
├── doc/
├── server/
│   └── user_registration.py
├── .env
└── .gitignore
```

---

## ▶️ Running the Server

From the **root directory** of your project, run:

```bash
uvicorn server.user_registration:app --reload
```

Then open your browser or API tool (like Postman) and go to:

👉 **http://127.0.0.1:8000/docs**

You’ll find the interactive Swagger UI where you can test the `/registro` endpoint.

---

## 🧪 Example Request

**Endpoint:** `POST /registro`

**Body:**
```json
{
  "name": "Molly",
  "email": "molly@example.com",
  "password": "UnaBuenaContraseña*1"
}
```

**Possible Responses:**
- ✅ `200 OK` → User created successfully.
- ⚠️ `400 Bad Request` → Invalid password or email already registered.
- ❌ `500 Internal Server Error` → Connection or database issue.

---

## 🧾 Notes

- Passwords must contain **at least 8 characters**, including **one uppercase**, **one number**, and **one special character (!@#$%^&*)**.
- All user data is stored in the Supabase table `usuarios`.
- Update `.env` credentials if Supabase project details change.

---

### 👩‍💻 Maintainers
Equipo 1 - Software Engineering  
University Project – 2025-2