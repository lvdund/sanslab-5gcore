from typing import List

from common.Snssai import Snssai
from pydantic import BaseModel


class NetworkSliceCond(BaseModel):
    snssaiList: List[Snssai]
    nsiList: List[str] = []

    class Config:
        extra = "forbid"
