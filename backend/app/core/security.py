from datetime import datetime, timedelta, timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:

    """
    Verify a plain-text password against a hashed password.

    Args:
        plain_password (str): The raw password entered by the user.
        hashed_password (str): The hashed password stored in the database.

    Returns:
        bool: True if the password matches the hash, otherwise False.
    """

    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:

    """
    Generate a bcrypt hash from a plain-text password.

    Args:
        password (str): The plain-text password to hash.

    Returns:
        str: Bcrypt hashed password.
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:

    """
    Create a JWT access token with an expiration claim (exp).

    Args:
        data (dict): Payload data to include in the JWT token.
        expires_delta (timedelta, optional): Custom expiration duration.
            If None, the default ACCESS_TOKEN_EXPIRE_MINUTES is used.

    Returns:
        str: Encoded JWT access token string.
    """

    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:

    """
    Decode and validate a JWT access token.

    Args:
        token (str): The JWT token string to decode.

    Returns:
        dict | None: Decoded token payload if valid, otherwise None.

    Notes:
        All JWTError exceptions are handled internally. Invalid or expired
        tokens return None instead of raising an exception.
    """

    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None