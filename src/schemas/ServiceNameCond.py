from pydantic import BaseModel

from schemas.ServiceName import ServiceName


class ServiceNameCond(BaseModel):
    serviceName: ServiceName

    class Config:
        extra = "forbid"
