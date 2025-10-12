````markdown
# 🛒 Market Prices & Login API

REST API built with **FastAPI** and **PostgreSQL** to:
- Query product prices in Medellín marketplaces.
- Manage user authentication (login, logout, password recovery).

---

## 🚀 Setup Guide

### 1️⃣ Prerequisites
- Python **3.13+** (compatible with 3.8+)
- **PostgreSQL** installed and running
- **pip** package manager

### 2️⃣ Create a virtual environment
```bash
python -m venv venv
````

Activate it:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **Linux/Mac:**

  ```bash
  source venv/bin/activate
  ```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Create a `.env` file

Inside the `server/` folder, create a `.env` file with the following variables:

```env
DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[database_name]
EMAIL_USER=
EMAIL_PASS=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```

🔹 Replace `[user]`, `[password]`, `[host]`, `[port]`, and `[database_name]` with your PostgreSQL credentials.
🔹 The other variables are used for authentication and email recovery.

### 5️⃣ Run the API

#### Option 1 (recommended)

```bash
uvicorn main:app --reload
```

#### Option 2 (alternative)

```bash
python -m uvicorn main:app --reload
```

✅ API available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
✅ ReDoc docs at: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🧱 Project Structure

```
server/
├── routers/              # Endpoints by module (e.g. auth, prices)
├── models.py             # SQLAlchemy models
├── database.py           # Database connection and session setup
├── main.py               # Application entry point
└── requirements.txt      # Project dependencies
```

---

## 🔑 Authentication Endpoints

### `/auth/login`

**POST**

**Body:**

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

📌 After login, use the `access_token` for authorized requests.

**Account Lock Test:**

* Enter a wrong password **3 times** to lock the account.
* A recovery email will be sent.

---

### `/auth/logout`

**POST**

**Header:**

```
Bearer <access_token>
```

**Response:**

```json
{ "message": "Sesión cerrada correctamente" }
```

---

### `/password/recover`

**POST**

**Body:**

```json
{
  "correo": "user@example.com"
}
```

**Response:**

```json
{ "message": "Correo de recuperación de contraseña enviado exitosamente" }
```

---

### `/password/reset/{token}`

**POST**

**Body:**

```json
{
  "nueva_contrasena": "newpassword123"
}
```

**Response:**

```json
{ "message": "Contraseña restablecida exitosamente" }
```

---

## 💰 Prices Endpoints

### `GET /`

Check that the API is running.

### `GET /prices/latest/`

Get the most recent price of a product in a marketplace.
**Parameters:**

* `product_name`
* `market_name`

### `GET /prices/options/`

Get combined list of products and marketplaces.

### `GET /prices/productos/`

List all available products.

### `GET /prices/plazas/medellin/`

List all Medellín marketplaces.

---

## 🗃️ Database Setup

### Required Tables

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

### Sample Data

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

### Code style

* Follow **PEP 8**
* Use **type hints** and **docstrings**
* Prefer descriptive variable names

### API design

* Consistent JSON responses
* Semantic HTTP status codes
* Documented endpoints via FastAPI decorators

---

## ⚠️ Common Troubleshooting

### `uvicorn` not running

Try:

```bash
python -m uvicorn main:app --reload
```

### Database connection error

* Verify PostgreSQL is running
* Check `.env` credentials
* Ensure database exists and user has permissions

### `ModuleNotFoundError`

Make sure you’ve activated your environment and installed dependencies:

```bash
pip install -r requirements.txt
```

---

📘 **Author:** Plaze Development Team
🔐 **Includes:** Authentication, Email Recovery & Market Prices API

```



