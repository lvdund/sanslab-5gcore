from pydantic import BaseModel

from .DateTime import DateTime
from .GlobalRanNodeId import GlobalRanNodeId
from .Ncgi import Ncgi
from .Tai import Tai


class NrLocation(BaseModel):
    tai: Tai
    ncgi: Ncgi
    ignoreNcgi: bool = None
    ageOfLocationInformation: int = None
    ueLocationTimestamp: DateTime = None
    geographicalInformation: str = None
    geodeticInformation: str = None
    globalGnbId: GlobalRanNodeId = None
