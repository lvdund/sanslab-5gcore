from pydantic import BaseModel


class TwapId(BaseModel):
    ssId: str
    bssId: str = None
    civicAddress: bytes = None
