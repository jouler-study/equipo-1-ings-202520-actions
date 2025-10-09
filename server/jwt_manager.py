# jwt_manager.py
"""
JWT manager: create and verify JWT access tokens.
Keep secrets out of source code in production (use environment variables).
"""

from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from uuid import uuid4

load_dotenv()

# Get secret and algorithm from environment (fallback values for local dev)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
# Default token lifetime in minutes
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    Create a signed JWT token with an expiration time.
    Args:
        data (dict): payload data to include (e.g. {"sub": user_email, "rol": "usuario"})
        expires_delta (timedelta | None): how long the token is valid
    Returns:
        str: encoded JWT
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({
        "exp": expire,              # Expiration time of the token
        "iat": datetime.utcnow(),   # Issued at: when the token was created
        "jti": str(uuid4())         # Unique token identifier to ensure each token is distinct
    })
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> dict:
    """
    Verify and decode a JWT token.
    Raises a JWTError (from python-jose) if invalid or expired.
    Returns the decoded payload (dict) when valid.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        # Let caller handle the exception (e.g., raise HTTPException)
        raise e
