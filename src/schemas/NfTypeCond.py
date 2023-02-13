from pydantic import BaseModel

from src.schemas.NFType import NFType


class NfTypeCond(BaseModel):
    nfType: NFType

    class Config:
        extra = "forbid"
