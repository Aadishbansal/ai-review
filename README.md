# PR Agent Demo App

A simple Python auth + user API app used to demo PR-Agent code review.

## Structure
- `src/auth.py` - Password hashing and session token generation
- `src/database.py` - SQLite DB helpers
- `src/api.py` - Login and session management
- `tests/` - Unit tests

## Setup
```bash
pip install pytest
pytest tests/
```
