import hashlib
import random
import secrets


# TRUE POSITIVE: weak hash algorithm — MD5 used for password hashing
def hash_password_legacy(password: str) -> str:
    return hashlib.md5(password.encode()).hexdigest()


# FALSE POSITIVE TEST: random.choices for non-security UI display
# Should NOT fire — random.choices removed from insecure_random rule
DISPLAY_THEMES = ["light", "dark", "high-contrast", "sepia"]

def pick_random_theme() -> str:
    return random.choices(DISPLAY_THEMES)[0]


# GOOD PATTERN: secrets module for actual token generation
def generate_api_token() -> str:
    return secrets.token_urlsafe(32)
