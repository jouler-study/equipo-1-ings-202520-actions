from fastapi import FastAPI
import httpx
import random

app = FastAPI(title="Load Balancer Simulator")

# List of backend instances (different ports)
BACKENDS = [
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8001",
]

@app.get("/{path:path}")
async def proxy(path: str):
    """Forward the GET request to a random instance"""
    backend = random.choice(BACKENDS)
    url = f"{backend}/{path}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            return response.json()
        except Exception as e:
            return {"error": f"Fallo en {backend}", "details": str(e)}