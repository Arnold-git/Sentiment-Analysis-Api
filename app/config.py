from pydantic import AnyHttpUrl, BaseSettings, validator
from typing import List, Union
from dotenv import load_dotenv


class Settings(BaseSettings):
    PROJECT_NAME: str = "SentimentApi"
    API_V1_STR: str = "/api/v1"
    SERVER_NAME: str = "SentimentApi"
    SERVER_HOST: AnyHttpUrl = "http://localhost:8000"
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

load_dotenv()
settings = Settings()