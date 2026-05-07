import os


DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
