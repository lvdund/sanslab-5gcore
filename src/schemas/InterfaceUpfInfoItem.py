from typing import List

from common.Ipv4Addr import Ipv4Addr
from common.Ipv6Addr import Ipv6Addr
from pydantic import BaseModel

from schemas.Fqdn import Fqdn
from schemas.UPInterfaceType import UPInterfaceType


class InterfaceUpfInfoItem(BaseModel):
    interfaceType: UPInterfaceType
    ipv4EndpointAddresses: List[Ipv4Addr] = None
    ipv6EndpointAddresses: List[Ipv6Addr] = None
    endpointFqdn: Fqdn = None
    networkInstance: str = None
