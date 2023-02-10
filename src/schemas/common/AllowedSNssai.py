from typing import List

from pydantic import BaseModel

from .NsiInformation import NsiInformation
from .Snssai import Snssai


class AllowedSNssai(BaseModel):
    allowedSNssai: Snssai
    nsiInformation: List[NsiInformation] = None
    mappedHomeSNssai: Snssai = None
