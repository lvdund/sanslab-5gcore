from typing import List

from common.AmfRegionId import AmfRegionId
from common.AmfSetId import AmfSetId
from common.Guami import Guami
from common.Tai import Tai
from pydantic import BaseModel

from schemas.N2InterfaceAmfInfo import N2InterfaceAmfInfo


class AmfInfo(BaseModel):
    amfRegionId: AmfRegionId
    amfSetId: AmfSetId
    guamiList: List[Guami]
    taiList: List[Tai] = None
    backupInfoAmfFailure: List[Guami] = None
    backupInfoAmfRemoval: List[Guami] = None
    n2InterfaceAmfInfo: N2InterfaceAmfInfo = None
