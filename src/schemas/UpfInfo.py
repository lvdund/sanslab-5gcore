from typing import List

from src.schemas.common.PduSessionType import PduSessionType
from pydantic import BaseModel

from src.schemas.InterfaceUpfInfoItem import InterfaceUpfInfoItem
from src.schemas.sNssaiSmfInfoItem import sNssaiSmfInfoItem


class UpfInfo(BaseModel):
    sNssaiSmfInfoList: List[sNssaiSmfInfoItem]
    smfServingArea: List[str] = None
    interfaceUpfInfoList: List[InterfaceUpfInfoItem] = None
    iwkEpsInd: bool = None
    pduSessionTypes: List[PduSessionType] = None
