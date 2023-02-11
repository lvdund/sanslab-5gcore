from typing import List

from common.PduSessionType import PduSessionType
from pydantic import BaseModel

from schemas.InterfaceUpfInfoItem import InterfaceUpfInfoItem
from schemas.sNssaiSmfInfoItem import sNssaiSmfInfoItem


class UpfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    smfServingArea: List[str] = None
    interfaceUpfInfoList: List[InterfaceUpfInfoItem] = None
    iwkEpsInd: bool = None
    pduSessionTypes: List[PduSessionType] = None
