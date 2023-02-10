from pydantic import BaseModel

from .BitRate import BitRate


class Ambr(BaseModel):
    uplink: BitRate
    downlink: BitRate
