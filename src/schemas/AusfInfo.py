from typing import List

from src.schemas.common.NfGroupId import NfGroupId
from pydantic import BaseModel

from src.schemas.SupiRange import SupiRange


class AusfInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = []
    routingIndicators: List[str] = []
