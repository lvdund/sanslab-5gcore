from pydantic import BaseModel


class ChfServiceInfo(BaseModel):
    primaryChfServiceInstance: str = None
    secondaryChfServiceInstance: str = None
