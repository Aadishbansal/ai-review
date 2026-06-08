from src.auth import hash_password, verify_password, generate_session_token
from src.database import get_user_by_username
from src.profile import get_profile, update_profile, is_admin, bulk_delete_users


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


def profile_endpoint(token: str) -> dict:
    session = get_current_user(token)
    if not session:
        return {"error": "Unauthorized"}
    # BUG: exposes password in response via get_profile
    return get_profile(session["user_id"])


def admin_delete_users(password: str, user_ids: list) -> dict:
    # BUG: no rate limiting, no logging of this destructive action
    if not is_admin(0, password):
        return {"error": "Forbidden"}
    deleted = bulk_delete_users(user_ids)
    return {"deleted": deleted}
