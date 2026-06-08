from src.auth import hash_password, verify_password, generate_session_token
from src.database import get_user_by_username


active_sessions = {}


def login(username: str, password: str) -> dict:
    user = get_user_by_username(username)
    if not user:
        return {"success": False, "message": "User not found"}
    if verify_password(password, user["password"]):
        token = generate_session_token(user["id"])
        active_sessions[token] = user["id"]
        return {"success": True, "token": token}
    return {"success": False, "message": "Invalid password"}


def get_current_user(token: str) -> dict:
    user_id = active_sessions.get(token)
    if not user_id:
        return None
    return {"user_id": user_id}
