from typing import List

from common.PlmnId import PlmnId
from common.Snssai import Snssai
from pydantic import BaseModel


class PlmnSnssai(BaseModel):
    plmnId: PlmnId
    sNssaiList: List[Snssai]
