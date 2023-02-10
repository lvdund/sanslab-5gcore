
from pydantic import BaseModel

from .Nid import Nid
from .NrCellId import NrCellId
from .PlmnId import PlmnId


class Ncgi(BaseModel):
    plmnId: PlmnId
    nrCellId: NrCellId
    nid: Nid = None
