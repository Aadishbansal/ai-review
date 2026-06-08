import hashlib
import time


def hash_password(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


def verify_password(password: str, hashed: str) -> bool:
    return hash_password(password) == hashed


def generate_session_token(user_id: int) -> str:
    raw = f"{user_id}-{time.time()}"
    return hashlib.md5(raw.encode()).hexdigest()
