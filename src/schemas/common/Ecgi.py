from pydantic import BaseModel

from .EutraCellId import EutraCellId
from .Nid import Nid
from .PlmnId import PlmnId


class Ecgi(BaseModel):
    plmnId: PlmnId
    eutraCellId: EutraCellId
    nid: Nid = None
