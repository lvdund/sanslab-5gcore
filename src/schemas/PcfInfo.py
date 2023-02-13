from typing import List

from src.schemas.common.DiameterIdentity import DiameterIdentity
from src.schemas.common.Dnn import Dnn
from pydantic import BaseModel

from src.schemas.SupiRange import SupiRange


class PcfInfo(BaseModel):
    dnnList: List[Dnn] = None
    supiRanges: List[SupiRange] = None
    rxDiamHost: DiameterIdentity = None
    rxDiamRealm: DiameterIdentity = None
