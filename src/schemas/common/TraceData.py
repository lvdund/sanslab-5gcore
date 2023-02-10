
from pydantic import BaseModel

from .Ipv4Addr import Ipv4Addr
from .Ipv6Addr import Ipv6Addr
from .TraceDepth import TraceDepth


class TraceData(BaseModel):
    traceRef: str
    traceDepth: TraceDepth
    neTypeList: str
    eventList: str
    collectionEntityIpv4Addr: Ipv4Addr = None
    collectionEntityIpv6Addr: Ipv6Addr = None
    interfaceList: str = None
