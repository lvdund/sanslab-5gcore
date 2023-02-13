from typing import List

from src.schemas.common.AccessType import AccessType
from src.schemas.common.Tai import Tai
from pydantic import BaseModel

from src.schemas.Fqdn import Fqdn
from src.schemas.sNssaiSmfInfoItem import sNssaiSmfInfoItem
from src.schemas.TaiRange import TaiRange


class SmfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    taiList: List[Tai] = None
    taiRangeList: List[TaiRange] = None
    pgwFqdn: Fqdn = None
    accessType: List[AccessType] = None
