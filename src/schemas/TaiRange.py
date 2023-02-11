from typing import List

from common.PlmnId import PlmnId
from pydantic import BaseModel

from schemas.TacRange import TacRange


class TaiRange(BaseModel):
    plmnId: PlmnId
    tacRangeList: List[TacRange]
