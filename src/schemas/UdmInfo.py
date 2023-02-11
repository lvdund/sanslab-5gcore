from typing import List

from common.NfGroupId import NfGroupId
from pydantic import BaseModel

from schemas.IdentityRange import IdentityRange
from schemas.SupiRange import SupiRange


class UdmInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = None
    gpsiRanges: List[IdentityRange] = None
    externalGroupIdentifiersRanges: List[IdentityRange] = None
    routingIndicators: List[str] = None
