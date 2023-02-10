from pydantic import BaseModel

from .Uinteger import Uinteger


class Snssai(BaseModel):
    sst: Uinteger
    sd: str
