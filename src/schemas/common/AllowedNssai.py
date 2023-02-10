from typing import List

from pydantic import BaseModel

from .AllowedSNssai import AllowedSNssai


class AllowedNssai(BaseModel):
    allowedSNssai: List[AllowedSNssai]
