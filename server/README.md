# 🛒 Market Prices & User Registration API

REST API built with **FastAPI** and **PostgreSQL/Supabase** to manage user registration, authentication, price queries, and marketplace data in Medellín.

---

## ✨ Features

- **User Registration** with secure Argon2 password hashing
- **User Authentication** (login, logout, password recovery)
- **Price Queries** for products in Medellín marketplaces
- **Email Validation** and duplicate checking
- **Account Security** with lockout after failed attempts
- **JWT-based Authorization** for protected endpoints
- **Supabase Integration** for scalable database operations

---

## 🚀 Quick Start

### Prerequisites

- Python **3.11+** (compatible with 3.8+)
- **PostgreSQL** installed and running (or **Supabase** account)
- **pip** package manager
- Access to a **Supabase** project (for user registration)

### 1️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

**Activate it:**

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **Linux/Mac:**
  ```bash
  source venv/bin/activate
  ```

### 2️⃣ Install Dependencies

```bash
pip install fastapi "uvicorn[standard]" supabase passlib[argon2] python-dotenv "pydantic[email]" postgresql
```

If you encounter errors with bcrypt:
```bash
pip install --upgrade passlib bcrypt
```

### 3️⃣ Create Environment Configuration

Inside the `server/` folder, create a `.env` file with:

```env
# PostgreSQL / Primary Database
DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[database_name]

# Supabase (for user registration)
SUPABASE_URL=https://YOUR_PROJECT_ID.supabase.co
SUPABASE_KEY=YOUR_SUPABASE_API_KEY

# Email Configuration (for password recovery)
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_app_password

# JWT Authentication
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

⚠️ **Important:** Ensure `SUPABASE_URL` begins with `https://` to avoid connection errors.

### 4️⃣ Run the API

**Option 1 (if uvicorn is in PATH):**
```bash
uvicorn main:app --reload
```

**Option 2 (recommended, especially for Windows):**
```bash
python -m uvicorn main:app --reload
```

✅ API available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
✅ ReDoc documentation at: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 📁 Project Structure

```
EQUIPO-1-INGS-202520/
├── client/
├── doc/
├── server/
│   ├── routers/              # Endpoints by module (auth, prices, registration)
│   ├── models.py             # SQLAlchemy models
│   ├── database.py           # Database connection and session setup
│   ├── user_registration.py  # User registration logic (Supabase)
│   ├── main.py               # Application entry point
│   ├── requirements.txt      # Project dependencies
│   └── .env                  # Environment variables
├── .gitignore
└── README.md
```

---

## 🔐 Authentication & User Management Endpoints

### User Registration

#### `POST /registro`

Create a new user account.

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "UnaBuenaContraseña*1"
}
```

**Password Requirements:**
- Minimum 8 characters
- At least one uppercase letter
- At least one number
- At least one special character (!@#$%^&*)

**Responses:**
- `200 OK` → User created successfully
- `400 Bad Request` → Invalid password or email already registered
- `422 Unprocessable Entity` → Validation error
- `503 Service Unavailable` → Database connection issue
- `500 Internal Server Error` → Unexpected error

---

### User Login

#### `POST /auth/login`

Authenticate user and obtain JWT token.

**Request Body:**
```json
{
  "correo": "user@example.com",
  "contrasena": "1234"
}
```

**Response:**
```json
{
  "message": "Inicio de sesión exitoso",
  "user": "user@example.com",
  "role": "usuario",
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

📌 Use the `access_token` in the `Authorization: Bearer <token>` header for protected requests.

**Account Security:**
- After 3 failed login attempts, the account is locked
- A password recovery email will be sent automatically

---

### User Logout

#### `POST /auth/logout`

Terminate the user session.

**Headers:**
```
Authorization: Bearer <access_token>
```

**Response:**
```json
{
  "message": "Sesión cerrada correctamente"
}
```

---

### Password Recovery

#### `POST /password/recover`

Request a password reset email.

**Request Body:**
```json
{
  "correo": "user@example.com"
}
```

**Response:**
```json
{
  "message": "Correo de recuperación de contraseña enviado exitosamente"
}
```

---

#### `POST /password/reset/{token}`

Reset password using recovery token.

**Request Body:**
```json
{
  "nueva_contrasena": "newpassword123"
}
```

**Response:**
```json
{
  "message": "Contraseña restablecida exitosamente"
}
```

---

## 💰 Market Prices Endpoints

### Health Check

#### `GET /`

Verify API is running.

---

### Latest Product Prices

#### `GET /prices/latest/`

Get the most recent price of a product in a specific marketplace.

**Query Parameters:**
- `product_name` (string) - Name of the product
- `market_name` (string) - Name of the marketplace

**Example:** `GET /prices/latest/?product_name=Tomate&market_name=Minorista`

---

### Available Options

#### `GET /prices/options/`

Get combined list of all available products and marketplaces.

---

### List All Products

#### `GET /prices/productos/`

Retrieve all available products in the database.

---

### List Medellín Marketplaces

#### `GET /prices/plazas/medellin/`

Retrieve all registered marketplaces in Medellín.

---

## 🗃️ Database Setup

### PostgreSQL Tables

Create the following tables in your PostgreSQL database:

```sql
CREATE TABLE productos (
    producto_id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL UNIQUE
);

CREATE TABLE plazas_mercado (
    plaza_id SERIAL PRIMARY KEY,
    nombre VARCHAR NOT NULL,
    ciudad VARCHAR NOT NULL
);

CREATE TABLE precios (
    precio_id SERIAL PRIMARY KEY,
    producto_id INTEGER NOT NULL REFERENCES productos(producto_id),
    plaza_id INTEGER NOT NULL REFERENCES plazas_mercado(plaza_id),
    precio_por_kg DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL
);
```

### Supabase Tables (User Registration)

Supabase will automatically handle the `usuarios` table when you set up the project. Ensure it includes:
- `id` (UUID) - Primary key
- `email` (VARCHAR) - User email, unique
- `name` (VARCHAR) - User full name
- `password_hash` (VARCHAR) - Argon2 hashed password
- `created_at` (TIMESTAMP) - Registration date

---

### Sample Data (PostgreSQL)

```sql
INSERT INTO productos (nombre) VALUES 
    ('Tomate'), ('Papa'), ('Cebolla');

INSERT INTO plazas_mercado (nombre, ciudad) VALUES 
    ('Minorista', 'Medellín'),
    ('La América', 'Medellín');

INSERT INTO precios (producto_id, plaza_id, precio_por_kg, fecha) VALUES 
    (1, 1, 3500.00, CURRENT_DATE),
    (2, 1, 2800.00, CURRENT_DATE);
```

---

## 🧰 Development Standards

### Code Style

- Follow **PEP 8** conventions
- Use **type hints** for all function parameters and returns
- Include **docstrings** for all functions and classes
- Use descriptive variable names

### API Design

- Consistent JSON responses across endpoints
- Semantic HTTP status codes (200, 201, 400, 401, 403, 404, 500, etc.)
- Documented endpoints via FastAPI decorators
- Input validation via Pydantic models

### Security Best Practices

- Passwords hashed with **Argon2**, never stored or returned in plain text
- JWT tokens for stateless authentication
- Environment variables for sensitive data (no hardcoding)
- Account lockout after failed login attempts
- Email verification for password recovery

---

## ⚠️ Troubleshooting

### Uvicorn Not Running

Try using the module execution approach:
```bash
python -m uvicorn main:app --reload
```

### Database Connection Error

- Verify PostgreSQL/Supabase service is running
- Check `.env` credentials are correct
- Ensure the database exists and user has permissions
- For Supabase, verify `SUPABASE_URL` format (must start with `https://`)

### Module Import Error (`ModuleNotFoundError`)

Ensure virtual environment is activated and dependencies installed:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Supabase Connection Issues

- Verify `SUPABASE_URL` and `SUPABASE_KEY` in `.env`
- Confirm Supabase project is active and accessible
- Check network connectivity and firewall settings

### Invalid URL Error

```
supabase._sync.client.SupabaseException: Invalid URL
```

Solution: Ensure `SUPABASE_URL` in `.env` starts with `https://`

---

## 📝 Example Workflow

1. **Register a new user:**
   ```bash
   POST /registro
   {
     "name": "Molly",
     "email": "molly@example.com",
     "password": "SecurePass*123"
   }
   ```

2. **Login:**
   ```bash
   POST /auth/login
   {
     "correo": "molly@example.com",
     "contrasena": "SecurePass*123"
   }
   ```

3. **Query market prices (with token):**
   ```bash
   GET /prices/latest/?product_name=Tomate&market_name=Minorista
   Headers: Authorization: Bearer <access_token>
   ```

4. **Logout:**
   ```bash
   POST /auth/logout
   Headers: Authorization: Bearer <access_token>
   ```

---

## 🔒 Security Reminders

- ✅ Passwords are hashed with Argon2 before storage
- ✅ Password hashes are never returned in API responses
- ✅ JWT tokens expire after the configured time (`ACCESS_TOKEN_EXPIRE_MINUTES`)
- ✅ Failed login attempts trigger account lockout and recovery email
- ✅ All sensitive data must be in `.env` and never committed to version control
- ✅ Use `.gitignore` to exclude `.env` and `__pycache__/`

---

## 📚 References

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Supabase Documentation](https://supabase.com/docs)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [Passlib Security](https://passlib.readthedocs.io/)
- [JWT Authentication](https://tools.ietf.org/html/rfc7519)

---

**Author:** Plaze Development Team  
**Version:** 1.0.0  
**Last Updated:** October 2025  
🔐 Includes: User Registration, Authentication, Email Recovery & Market Prices API