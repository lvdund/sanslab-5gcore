from pydantic import BaseModel

from .PlmnId import PlmnId
from .Tac import Tac


class Tai(BaseModel):
    plmnId: PlmnId
    tac: Tac
