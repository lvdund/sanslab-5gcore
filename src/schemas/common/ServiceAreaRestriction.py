from typing import List

from pydantic import BaseModel

from .Area import Area
from .RestrictionType import RestrictionType
from .Uinteger import Uinteger


class ServiceAreaRestriction(BaseModel):
    restrictionType: RestrictionType = None
    areas: List[Area] = None
    maxNumOfTAs: Uinteger = None
    maxNumOfTAsForNotAllowedAreas: Uinteger = None
