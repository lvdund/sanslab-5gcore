from typing import List

from src.schemas.common.PlmnId import PlmnId
from pydantic import BaseModel

from src.schemas.TacRange import TacRange


class TaiRange(BaseModel):
    plmnId: PlmnId
    tacRangeList: List[TacRange]
