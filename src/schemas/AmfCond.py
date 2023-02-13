from src.schemas.common.AmfRegionId import AmfRegionId
from src.schemas.common.AmfSetId import AmfSetId
from pydantic import BaseModel


class AmfCond(BaseModel):
    amfSetId: AmfSetId = None
    amfRegionId: AmfRegionId = None

    class Config:
        extra = "forbid"
