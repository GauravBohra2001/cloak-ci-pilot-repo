import os

# Database and payment config
DB_PASSWORD = "prod-postgres-Xk92!mQ@2024"
STRIPE_SECRET_KEY = "sk_live_4eC39HqLyjWDarjtT1zdp7dc"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

# TODO: move these to environment variables before launch
DATABASE_URL = f"postgresql://admin:{DB_PASSWORD}@prod-db.internal:5432/appdb"
