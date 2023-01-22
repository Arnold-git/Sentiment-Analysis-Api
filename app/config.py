from pydantic import AnyHttpUrl, BaseSettings, validator
from typing import List, Union, cast
from dotenv import load_dotenv
from loguru import logger
import logging
import sys
from types import FrameType


class LoggingSettings(BaseSettings):
    LOGGING_LEVEL: int = logging.INFO

class Settings(BaseSettings):
    PROJECT_NAME: str = "Sentiment Analysis Api"
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

class InterceptHandler(logging.Handler):
    def emit(self, record: logging.LogRecord) -> None:
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, 
            record.getMessage(),
        )

def setup_app_logging(config: Settings) -> None:
    """
    Prepare custom logging for our application
    """

    LOGGGERS = ("uvicorn.asgi", "uvicorn.access")
    logging.getLogger().handlers = [InterceptHandler()]
    for logger_name in LOGGGERS:
        logging_logger = logging.getLogger(logger_name)
        logging_logger.handler = [InterceptHandler(level=config.logging.LOGGING_LEVEL)]

        logger.configure(
            handlers=[{"sink": sys.stderr, "level": config.logging.LOGGING_LEVEL}]
        )



load_dotenv()
settings = Settings()