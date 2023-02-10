
from pydantic import BaseModel

from .Auts import Auts
from .Rand import Rand


class ResynchronizationInfo(BaseModel):
    rand: Rand
    auts: Auts
