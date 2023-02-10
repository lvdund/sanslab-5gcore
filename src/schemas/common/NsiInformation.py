from pydantic import BaseModel

from .Fqdn import Fqdn
from .NsiId import NsiId


class NsiInformation(BaseModel):
    nrfId: Fqdn
    nsiId: NsiId = None
