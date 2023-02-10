from pydantic import BaseModel

from .ENbId import ENbId
from .GNbId import GNbId
from .N3IwfId import N3IwfId
from .NgeNbId import NgeNbId
from .Nid import Nid
from .PlmnId import PlmnId
from .TngfId import TngfId
from .WAgfId import WAgfId


class GlobalRanNodeId(BaseModel):
    plmnId: PlmnId
    n3IwfId: N3IwfId = None
    gNbId: GNbId = None
    ngeNbId: NgeNbId = None
    wagfId: WAgfId = None
    tngfId: TngfId = None
    nid: Nid = None
    eNbId: ENbId = None
