from typing import List

from pydantic import BaseModel

from schemas.IdentityRange import IdentityRange
from schemas.PlmnRange import PlmnRange
from schemas.SupiRange import SupiRange


class ChfInfo(BaseModel):
    supiRangeList: List[SupiRange] = None
    gpsiRangeList: List[IdentityRange] = None
    plmnRangeList: List[PlmnRange] = None
