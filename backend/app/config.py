from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    """Application settings loaded from environment variables"""
    
    # App Configuration
    APP_NAME: str = "QueryForge API"
    VERSION: str = "0.1.0"
    DEBUG: bool = True
    ENVIRONMENT: str = "development"
    
    # CORS
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:3001"]
    
    # Database (Neon PostgreSQL)
    DATABASE_URL: str = "postgresql+asyncpg://user:password@localhost/queryforge"
    
    # Redis (Upstash)
    REDIS_URL: str = "redis://localhost:6379"
    
    # Authentication (Clerk)
    CLERK_SECRET_KEY: str = ""
    CLERK_PUBLISHABLE_KEY: str = ""
    
    # AI (Google Gemini)
    GEMINI_API_KEY: str = ""
    
    # Email (Resend)
    RESEND_API_KEY: str = ""
    
    # Monitoring (Sentry)
    SENTRY_DSN: str = ""
    
    # JWT Configuration
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
