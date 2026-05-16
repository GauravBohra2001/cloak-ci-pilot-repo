import jwt


# TRUE POSITIVE: hardcoded signing key
JWT_SIGNING_KEY = "dev-only-secret-key-do-not-use-in-production"


# TRUE POSITIVE: JWT signature verification disabled
def decode_without_verification(token: str) -> dict:
    return jwt.decode(token, options={"verify_signature": False})


# TRUE POSITIVE: JWT none algorithm
def encode_none_algorithm(payload: dict) -> str:
    return jwt.encode(payload, algorithm="none", key="")
