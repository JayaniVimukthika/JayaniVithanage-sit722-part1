import os

class Settings:
    DATABASE_URL: str = os.getenv("postgresql://postgresql_aw66_user:MwxzGjRp2zudQKkrx9DdPkZJn6R3zS1t@dpg-cr4of5l2ng1s73e4ilpg-a.oregon-postgres.render.com/postgresql_aw66")

settings = Settings()
