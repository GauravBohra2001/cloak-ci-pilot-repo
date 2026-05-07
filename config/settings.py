import os


DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["*"]
CORS_ALLOW_ALL_ORIGINS = True
