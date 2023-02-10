from typing import List

from pydantic import BaseModel

from .Ecgi import Ecgi
from .GlobalRanNodeId import GlobalRanNodeId
from .Ncgi import Ncgi
from .PresenceState import PresenceState
from .Tai import Tai


class PresenceInfo(BaseModel):
    praId: str = None
    presenceState: PresenceState = None
    trackingAreaList: List[Tai] = None
    ecgiList: List[Ecgi] = None
    ncgiList: List[Ncgi] = None
    globalRanNodeIdList: List[GlobalRanNodeId] = None
