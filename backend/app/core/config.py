from pydantic_settings import BaseSettings
from pydantic import field_validator
from typing import List



class Settings(BaseSettings):

    """
    Application settings loaded from environment variables.
    
    Required fields: SECRET_KEY, DATABASE_URL, REDIS_URL
    Optional fields: OPENAI_API_KEY, HUGGINGFACE_TOKEN, CELERY_BROKER_URL, CELERY_RESULT_BACKEND
    """

    APP_NAME: str = "WHOOP Clone"
    DEBUG: bool = False
    API_V1_PREFIX: str = "/api/v1"
    
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    DATABASE_URL: str
    REDIS_URL: str
    
    CORS_ORIGINS: List[str] = []
    
    OPENAI_API_KEY: Optional[str] = None
    HUGGINGFACE_TOKEN: Optional[str] = None
    MODEL_NAME: str = "meta-llama/Llama-2-7b-chat-hf"
    
    CELERY_BROKER_URL: str = ""
    CELERY_RESULT_BACKEND: str = ""
    
    @field_validator('SECRET_KEY')
    @classmethod
    def validate_secret_key(cls, v):
        if len(v) < 32:
            raise ValueError('SECRET_KEY must be at least 32 characters')
        return v
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()