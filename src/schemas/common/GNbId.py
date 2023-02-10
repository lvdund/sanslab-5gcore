from pydantic import BaseModel


class GNbId(BaseModel):
    bitLength: int
    gNBValue: str
