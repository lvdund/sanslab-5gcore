from pydantic import BaseModel

from .HfcNId import HfcNId


class HfcNodeId(BaseModel):
    hfcNId: HfcNId
