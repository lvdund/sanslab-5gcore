from pydantic import BaseModel

from .AmfId import AmfId
from .PlmnId import PlmnId


class Guami(BaseModel):
    plmnId: PlmnId
    amfId: AmfId
