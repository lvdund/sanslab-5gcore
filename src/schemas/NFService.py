from typing import List

from src.schemas.common.DateTime import DateTime
from src.schemas.common.PlmnId import PlmnId
from src.schemas.common.Snssai import Snssai
from src.schemas.common.SupportedFeatures import SupportedFeatures
from src.schemas.common.UriScheme import UriScheme
from pydantic import BaseModel

from src.schemas.ChfServiceInfo import ChfServiceInfo
from src.schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from src.schemas.Fqdn import Fqdn
from src.schemas.IpEndPoint import IpEndPoint
from src.schemas.NFServiceStatus import NFServiceStatus
from src.schemas.NFServiceVersion import NFServiceVersion
from src.schemas.NFType import NFType
from src.schemas.ServiceName import ServiceName


class NFService(BaseModel):
    serviceInstanceID: str = None       # lvdund
    serviceName: ServiceName
    versions: List[NFServiceVersion]
    scheme: UriScheme
    nfServiceStatus: NFServiceStatus
    fqdn: Fqdn = None
    interPlmnFqdn: Fqdn = None
    ipEndPoints: List[IpEndPoint] = []
    apiPrefix: str = None
    defaultNotificationSubscriptions: List[DefaultNotificationSubscription] = []
    allowedPlmns: List[PlmnId] = []
    allowedNfTypes: List[NFType] = []
    allowedNfDomains: List[str] = []
    allowedNssais: List[Snssai] = []
    priority: int = None
    capacity: int = None
    load: int = None
    recoveryTime: DateTime = None
    chfServiceInfo: ChfServiceInfo = None
    supportedFeatures: SupportedFeatures = None
