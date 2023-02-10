from pydantic import BaseModel

from .DateTime import DateTime
from .Ecgi import Ecgi
from .GlobalRanNodeId import GlobalRanNodeId
from .Tai import Tai


class EutraLocation(BaseModel):
    tai: Tai
    ecgi: Ecgi
    ignoreEcgi: bool = None
    ageOfLocationInformation: int = None
    ueLocationTimestamp: DateTime = None
    geographicalInformation: str = None
    geodeticInformation: str = None
    globalNgenbId: GlobalRanNodeId = None
    globalENbId: GlobalRanNodeId = None
