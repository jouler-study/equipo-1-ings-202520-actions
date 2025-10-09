# Market Prices API 🚀

REST API to query product prices in Medellín marketplaces, built with FastAPI and PostgreSQL.

## What does this folder do?

This directory contains the project backend, which provides a REST API to:
- Query updated product prices in different marketplaces
- List all available products
- List all Medellín marketplaces
- Get combined options of products and markets in a single request

## How to install this part of the project?

### Prerequisites
- Python 3.13 or higher
- PostgreSQL installed and running
- pip (Python package manager)

### Installation steps

1. **Create a virtual environment** (recommended):
```bash
python -m venv venv
```

2. **Activate the virtual environment**:
   - Windows:
   ```bash
   venv\Scripts\activate
   ```
   - Linux/Mac:
   ```bash
   source venv/bin/activate
   ```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**:
   
   Create a `.env` file in the project root with the following content:
   ```env
   DATABASE_URL=postgresql://[user]:[password]@[host]:[port]/[database_name]
   ```
   
   **Example**:
   ```env
   DATABASE_URL=postgresql://myuser:mypassword@localhost:5432/market_prices_db
   ```
   
   Replace the values in brackets with your actual PostgreSQL credentials.

## How to run this part of the project?

### Option 1 (recommended):
```bash
uvicorn main:app --reload
```

### Option 2 (if the first one doesn't work):
```bash
python -m uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

### Interactive documentation

Once the server is running, you can access:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## What standards should be followed?

### Python code standards
- **PEP 8**: Style guide for Python code
- **Type hints**: Use type annotations when possible
- **Docstrings**: Document functions and classes using Google or NumPy format
- **Descriptive names**: Variables and functions should have clear and descriptive names

### Folder structure
```
server/
├── routers/          # Endpoints organized by module
├── models.py         # SQLAlchemy models
├── database.py       # Database configuration
├── main.py           # Application entry point
└── requirements.txt  # Project dependencies
```

### API conventions
- Use appropriate HTTP verbs (GET, POST, PUT, DELETE)
- Structured and consistent JSON responses
- Semantic HTTP status codes
- Endpoint documentation with FastAPI decorators

## What Python version does it use?

**Python 3.13** (compatible with 3.8+)

To check your Python version:
```bash
python --version
```

## What do I need for the database?

### Database requirements

1. **PostgreSQL** installed and running (version 12 or higher recommended)

2. **Table structure**:

   The database must have the following tables:

   ```sql
   -- Products table
   CREATE TABLE productos (
       producto_id SERIAL PRIMARY KEY,
       nombre VARCHAR NOT NULL UNIQUE
   );

   -- Marketplaces table
   CREATE TABLE plazas_mercado (
       plaza_id SERIAL PRIMARY KEY,
       nombre VARCHAR NOT NULL,
       ciudad VARCHAR NOT NULL
   );

   -- Prices table
   CREATE TABLE precios (
       precio_id SERIAL PRIMARY KEY,
       producto_id INTEGER NOT NULL REFERENCES productos(producto_id),
       plaza_id INTEGER NOT NULL REFERENCES plazas_mercado(plaza_id),
       precio_por_kg DECIMAL(10,2) NOT NULL,
       fecha DATE NOT NULL
   );
   ```

3. **Database connection**:
   
   Configure the `.env` file with the connection URL in format:
   ```
   postgresql://[user]:[password]@[host]:[port]/[database_name]
   ```
   
   **Parameters**:
   - `[user]`: Your PostgreSQL user
   - `[password]`: Your PostgreSQL password
   - `[host]`: Server address (usually `localhost`)
   - `[port]`: PostgreSQL port (default `5432`)
   - `[database_name]`: Your database name

### Sample data (optional)

To test the API, you can insert sample data:

```sql
-- Insert products
INSERT INTO productos (nombre) VALUES 
    ('Tomate'),
    ('Papa'),
    ('Cebolla');

-- Insert marketplaces
INSERT INTO plazas_mercado (nombre, ciudad) VALUES 
    ('Minorista', 'Medellín'),
    ('La América', 'Medellín');

-- Insert prices
INSERT INTO precios (producto_id, plaza_id, precio_por_kg, fecha) VALUES 
    (1, 1, 3500.00, CURRENT_DATE),
    (2, 1, 2800.00, CURRENT_DATE);
```

## Available endpoints

### `GET /`
Check that the API is working.

### `GET /prices/latest/`
Get the most recent price of a product in a specific marketplace.

**Parameters**:
- `product_name`: Product name (partial search)
- `market_name`: Marketplace name (partial search)

### `GET /prices/options/`
Get combined list of available products and marketplaces.

### `GET /prices/productos/`
List all available products.

### `GET /prices/plazas/medellin/`
List all Medellín marketplaces.

## Common troubleshooting

### Error running uvicorn
If `uvicorn main:app --reload` doesn't work, use:
```bash
python -m uvicorn main:app --reload
```

### Database connection error
Verify that:
- PostgreSQL is running
- Credentials in `.env` are correct
- The database exists
- The user has sufficient permissions

### ModuleNotFoundError
Make sure you have activated the virtual environment and run:
```bash
pip install -r requirements.txt
```