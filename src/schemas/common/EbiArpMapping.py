from pydantic import BaseModel

from .Arp import Arp
from .EpsBearerId import EpsBearerId


class EbiArpMapping(BaseModel):
    epsBearerId: EpsBearerId
    arp: Arp
