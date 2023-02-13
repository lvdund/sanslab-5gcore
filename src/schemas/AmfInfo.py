from typing import List

from src.schemas.common.AmfRegionId import AmfRegionId
from src.schemas.common.AmfSetId import AmfSetId
from src.schemas.common.Guami import Guami
from src.schemas.common.Tai import Tai
from pydantic import BaseModel

from src.schemas.N2InterfaceAmfInfo import N2InterfaceAmfInfo


class AmfInfo(BaseModel):
    amfRegionId: AmfRegionId
    amfSetId: AmfSetId
    guamiList: List[Guami]
    taiList: List[Tai] = None
    backupInfoAmfFailure: List[Guami] = None
    backupInfoAmfRemoval: List[Guami] = None
    n2InterfaceAmfInfo: N2InterfaceAmfInfo = None
