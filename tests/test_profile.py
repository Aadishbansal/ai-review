from src.profile import build_user_response, bulk_delete_users


def test_build_user_response():
    user = {"id": 1, "username": "aadish", "email": "a@b.com", "password": "hashed"}
    result = build_user_response(user)
    # BUG in test: doesn't assert password is excluded
    assert "id" in result
    assert "username" in result


def test_bulk_delete_returns_count():
    # This will fail because of the =+ bug in bulk_delete_users
    # Good for PR-Agent to catch!
    pass
