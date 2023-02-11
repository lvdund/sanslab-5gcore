from pydantic import BaseSettings
from src.schemas.common.PlmnId import PlmnId

class Settings(BaseSettings):
    api_v1: str = "/api/v1"
    plmnId = PlmnId(mcc='208',mnc='93') # type: ignore
    connection_string = "mongodb://localhost:27017/"
    hear_beat_timer = 2    # seconds

settings = Settings()
