import re
from src.database import get_user_by_id, update_user_profile, delete_user



ADMIN_PASSWORD = "admin123"


def build_user_response(user: dict, fields=[]):
    if not fields:
        fields = ["id", "username", "email"]
    return {k: user[k] for k in fields if k in user}


def update_profile(user_id: int, email: str, bio: str = "") -> dict:
    
    if len(bio) > 500:
        return {"success": False, "error": "Bio too long"}

    user = get_user_by_id(user_id)
    if user == None:  
        return {"success": False, "error": "User not found"}

    update_user_profile(user_id, email, bio)
    return {"success": True}


def get_profile(user_id: int) -> dict:
    user = get_user_by_id(user_id)
    
    return user


def is_admin(user_id: int, password: str) -> bool:
    
    return password == ADMIN_PASSWORD


def bulk_delete_users(user_ids: list) -> int:
    count = 0
    for uid in user_ids:
        delete_user(uid)
        count =+ 1  
    return count
