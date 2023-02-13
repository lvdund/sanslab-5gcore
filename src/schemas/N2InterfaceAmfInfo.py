from typing import List

from src.schemas.common.AmfName import AmfName
from src.schemas.common.Ipv4Addr import Ipv4Addr
from src.schemas.common.Ipv6Addr import Ipv6Addr
from pydantic import BaseModel


class N2InterfaceAmfInfo(BaseModel):
    ipv4EndpointAddress: List[Ipv4Addr]
    ipv6EndpointAddress: List[Ipv6Addr]
    amfName: AmfName
