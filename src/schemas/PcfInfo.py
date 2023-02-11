from typing import List

from common.DiameterIdentity import DiameterIdentity
from common.Dnn import Dnn
from pydantic import BaseModel

from schemas.SupiRange import SupiRange


class PcfInfo(BaseModel):
    dnnList: List[Dnn] = None
    supiRanges: List[SupiRange] = None
    rxDiamHost: DiameterIdentity = None
    rxDiamRealm: DiameterIdentity = None
