from pydantic import BaseModel

from .EutraLocation import EutraLocation
from .N3gaLocation import N3gaLocation
from .NrLocation import NrLocation


class UserLocation(BaseModel):
    eutraLocation: EutraLocation = None
    nrLocation: NrLocation = None
    n3gaLocation: N3gaLocation = None
