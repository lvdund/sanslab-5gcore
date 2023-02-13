from typing import List

from src.schemas.common.NfGroupId import NfGroupId
from pydantic import BaseModel

from src.schemas.DataSetId import DataSetId
from src.schemas.IdentityRange import IdentityRange
from src.schemas.SupiRange import SupiRange


class UdrInfo(BaseModel):
    groupId: NfGroupId = None
    supiRanges: List[SupiRange] = None
    gpsiRanges: List[IdentityRange] = None
    externalGroupIdentifiersRanges: List[IdentityRange] = None
    supportedDataSets: List[DataSetId] = None
