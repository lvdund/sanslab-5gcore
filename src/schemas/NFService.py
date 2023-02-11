from typing import List

from common.DateTime import DateTime
from common.PlmnId import PlmnId
from common.Snssai import Snssai
from common.SupportedFeatures import SupportedFeatures
from common.UriScheme import UriScheme
from pydantic import BaseModel

from schemas.ChfServiceInfo import ChfServiceInfo
from schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from schemas.Fqdn import Fqdn
from schemas.IpEndPoint import IpEndPoint
from schemas.NFServiceStatus import NFServiceStatus
from schemas.NFServiceVersion import NFServiceVersion
from schemas.NFType import NFType
from schemas.ServiceName import ServiceName


class NFService(BaseModel):
    serviceInstanceID: str
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
