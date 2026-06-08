from src.auth import hash_password, verify_password


def test_hash_password():
    hashed = hash_password("mysecret")
    assert hashed is not None
    assert len(hashed) == 32


def test_verify_password():
    hashed = hash_password("mysecret")
    assert verify_password("mysecret", hashed) is True
    assert verify_password("wrongpass", hashed) is False
