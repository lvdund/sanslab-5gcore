
from enum import Enum


class PresenceState(Enum):
    in_area = "IN_AREA"
    out_of_area = "OUT_OF_AREA"
    unknown = "UNKNOWN"
    inactive = "INACTIVE"
