from pydantic import BaseModel

from .Mcc import Mcc
from .Mnc import Mnc


class PlmnId(BaseModel):
    mcc: Mcc
    mnc: Mnc
