from common.Ipv4Addr import Ipv4Addr
from pydantic import BaseModel


class Ipv4AddressRange(BaseModel):
    start: Ipv4Addr
    end: Ipv4Addr
