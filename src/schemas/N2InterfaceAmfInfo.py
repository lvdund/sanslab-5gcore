from typing import List

from common.AmfName import AmfName
from common.Ipv4Addr import Ipv4Addr
from common.Ipv6Addr import Ipv6Addr
from pydantic import BaseModel


class N2InterfaceAmfInfo(BaseModel):
    ipv4EndpointAddress: List[Ipv4Addr]
    ipv6EndpointAddress: List[Ipv6Addr]
    amfName: AmfName
