from typing import List

from src.schemas.common.PlmnId import PlmnId
from src.schemas.common.Snssai import Snssai
from pydantic import BaseModel


class PlmnSnssai(BaseModel):
    plmnId: PlmnId
    sNssaiList: List[Snssai]
