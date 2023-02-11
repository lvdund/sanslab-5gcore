from common.Ipv4Addr import Ipv4Addr
from common.Ipv6Addr import Ipv6Addr
from pydantic import BaseModel

from schemas.TransportProtocol import TransportProtocol


class IpEndPoint(BaseModel):
    ipv4Address: Ipv4Addr = None
    ipv6Address: Ipv6Addr = None
    transport: TransportProtocol = None
    port: int = None
