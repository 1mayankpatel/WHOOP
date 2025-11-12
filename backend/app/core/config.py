from pydantic_settings import BaseSettings
from typing import List


class Settings(BaseSettings):
    APP_NAME: str = "WHOOP Clone"
    DEBUG: bool = True
    API_V1_PREFIX: str = "/api/v1"
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    DATABASE_URL: str
    REDIS_URL: str
    
    CORS_ORIGINS: List[str] = ["http://localhost:5173", "http://localhost:3000"]
    
    OPENAI_API_KEY: str = ""
    HUGGINGFACE_TOKEN: str = ""
    MODEL_NAME: str = "meta-llama/Llama-2-7b-chat-hf"
    
    CELERY_BROKER_URL: str = ""
    CELERY_RESULT_BACKEND: str = ""
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()