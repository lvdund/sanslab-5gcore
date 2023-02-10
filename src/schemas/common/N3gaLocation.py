from pydantic import BaseModel

from .Gci import Gci
from .Gli import Gli
from .HfcNodeId import HfcNodeId
from .Ipv4Addr import Ipv4Addr
from .Ipv6Addr import Ipv6Addr
from .LineType import LineType
from .Tai import Tai
from .TnapId import TnapId
from .TwapId import TwapId
from .Uinteger import Uinteger


class N3gaLocation(BaseModel):
    n3gppTai: Tai = None
    n3IwfId: str = None
    ueIpv4Addr: Ipv4Addr = None
    ueIpv6Addr: Ipv6Addr = None
    portNumber: Uinteger = None
    tnapId: TnapId = None
    twapId: TwapId = None
    hfcNodeId: HfcNodeId = None
    gli: Gli = None
    w5gbanLineType: LineType = None
    gci: Gci = None
