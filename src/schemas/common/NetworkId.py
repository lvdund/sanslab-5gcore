from pydantic import BaseModel

from .Mcc import Mcc
from .Mnc import Mnc


class NetworkId(BaseModel):
    mcc: Mcc = None
    mnc: Mnc = None
