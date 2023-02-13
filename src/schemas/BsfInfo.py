from typing import List

from src.schemas.common.Dnn import Dnn
from pydantic import BaseModel

from src.schemas.Ipv4AddressRange import Ipv4AddressRange
from src.schemas.Ipv6PrefixRange import Ipv6PrefixRange


class BsfInfo(BaseModel):
    ipv4AddressRanges: List[Ipv4AddressRange] = None
    dnnList: List[Dnn] = None
    ipDomainList: List[str] = None
    ipv6PrefixRanges: List[Ipv6PrefixRange] = None
