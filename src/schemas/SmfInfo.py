from typing import List

from common.AccessType import AccessType
from common.Tai import Tai
from pydantic import BaseModel

from schemas.Fqdn import Fqdn
from schemas.sNssaiSmfInfoItem import sNssaiSmfInfoItem
from schemas.TaiRange import TaiRange


class SmfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    taiList: List[Tai] = None
    taiRangeList: List[TaiRange] = None
    pgwFqdn: Fqdn = None
    accessType: List[AccessType] = None
