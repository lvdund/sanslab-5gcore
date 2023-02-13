from pydantic import BaseModel

from src.schemas.ServiceName import ServiceName


class ServiceNameCond(BaseModel):
    serviceName: ServiceName

    class Config:
        extra = "forbid"
