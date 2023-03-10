from pydantic import BaseSettings
from src.schemas.common.PlmnId import PlmnId, Mcc, Mnc


class Settings(BaseSettings):
    api_v1: str = "/api/v1"
    plmnId = PlmnId(mcc=Mcc('208'), mnc=Mnc('93'))  # type: ignore
    connection_string = "mongodb://localhost:27017/"
    hear_beat_timer = 10    # seconds


settings = Settings()
