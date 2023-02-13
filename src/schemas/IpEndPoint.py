from src.schemas.common.Ipv4Addr import Ipv4Addr
from src.schemas.common.Ipv6Addr import Ipv6Addr
from pydantic import BaseModel

from src.schemas.TransportProtocol import TransportProtocol


class IpEndPoint(BaseModel):
    ipv4Address: Ipv4Addr = None
    ipv6Address: Ipv6Addr = None
    transport: TransportProtocol = None
    port: int = None
