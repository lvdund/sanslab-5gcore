
from typing import List

from pydantic import BaseModel

from .AreaCode import AreaCode
from .Tac import Tac


class Area(BaseModel):
    tacs: List[Tac] = None
    areaCode: AreaCode = None
