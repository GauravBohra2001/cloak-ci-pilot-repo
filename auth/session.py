import os


JWT_SECRET = os.getenv("JWT_SECRET", "")


def load_auth_settings() -> dict:
    return {
        "jwt_secret_present": bool(JWT_SECRET),
        "session_cookie_secure": True,
        "session_cookie_httponly": True,
    }
