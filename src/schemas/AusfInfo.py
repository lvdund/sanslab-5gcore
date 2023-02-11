from typing import List

from common.NfGroupId import NfGroupId
from pydantic import BaseModel

from schemas.SupiRange import SupiRange


class AusfInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = []
    routingIndicators: List[str] = []
