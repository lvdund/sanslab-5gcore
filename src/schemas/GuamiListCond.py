from typing import List

from src.schemas.common.Guami import Guami
from pydantic import BaseModel


class GuamiListCond(BaseModel):
    guamiList: List[Guami]

    class Config:
        extra = "forbid"
