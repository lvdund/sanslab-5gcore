from common.Ipv6Prefix import Ipv6Prefix
from pydantic import BaseModel


class Ipv6PrefixRange(BaseModel):
    start: Ipv6Prefix
    end: Ipv6Prefix
