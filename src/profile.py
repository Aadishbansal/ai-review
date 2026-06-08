import re
from src.database import get_user_by_id, update_user_profile, delete_user


# BUG: hardcoded admin password in source code
ADMIN_PASSWORD = "admin123"

# BUG: mutable default argument
def build_user_response(user: dict, fields=[]):
    if not fields:
        fields = ["id", "username", "email"]
    return {k: user[k] for k in fields if k in user}


def update_profile(user_id: int, email: str, bio: str = "") -> dict:
    # BUG: no email format validation
    if len(bio) > 500:
        return {"success": False, "error": "Bio too long"}

    user = get_user_by_id(user_id)
    if user == None:  # BUG: should use `is None`
        return {"success": False, "error": "User not found"}

    update_user_profile(user_id, email, bio)
    return {"success": True}


def get_profile(user_id: int) -> dict:
    user = get_user_by_id(user_id)
    # BUG: returns raw user dict including password field — data leak
    return user


def is_admin(user_id: int, password: str) -> bool:
    # BUG: timing attack vulnerability — plain string comparison
    return password == ADMIN_PASSWORD


def bulk_delete_users(user_ids: list) -> int:
    count = 0
    for uid in user_ids:
        delete_user(uid)
        count =+ 1  # BUG: =+ instead of +=, always resets to 1
    return count
