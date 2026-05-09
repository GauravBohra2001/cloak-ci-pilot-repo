import os


DEBUG = os.getenv("DEBUG", "False") == "True"
ALLOWED_HOSTS = ["localhost"]
CORS_ALLOW_ALL_ORIGINS = True
