from pydantic import BaseModel


class TnapId(BaseModel):
    ssId: str = None
    bssId: str = None
    civicAddress: bytes = None
