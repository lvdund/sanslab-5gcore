from typing import List

from pydantic import BaseModel

from src.schemas.IdentityRange import IdentityRange
from src.schemas.PlmnRange import PlmnRange
from src.schemas.SupiRange import SupiRange


class ChfInfo(BaseModel):
    supiRangeList: List[SupiRange] = None
    gpsiRangeList: List[IdentityRange] = None
    plmnRangeList: List[PlmnRange] = None
