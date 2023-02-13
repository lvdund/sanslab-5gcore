from typing import List

from src.schemas.common.DateTime import DateTime
from src.schemas.common.Ipv4Addr import Ipv4Addr
from src.schemas.common.Ipv6Addr import Ipv6Addr
from src.schemas.common.NfInstanceId import NfInstanceId
from src.schemas.common.PlmnId import PlmnId
from src.schemas.common.Snssai import Snssai
from pydantic import BaseModel

from src.schemas.AmfInfo import AmfInfo
from src.schemas.AusfInfo import AusfInfo
from src.schemas.BsfInfo import BsfInfo
from src.schemas.ChfInfo import ChfInfo
from src.schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from src.schemas.Fqdn import Fqdn
from src.schemas.NFService import NFService
from src.schemas.NFStatus import NFStatus
from src.schemas.NFType import NFType
from src.schemas.NrfInfo import NrfInfo
from src.schemas.PcfInfo import PcfInfo
from src.schemas.PlmnSnssai import PlmnSnssai
from src.schemas.SmfInfo import SmfInfo
from src.schemas.UdmInfo import UdmInfo
from src.schemas.UdrInfo import UdrInfo
from src.schemas.UpfInfo import UpfInfo


class NFProfile(BaseModel):
    nfInstanceID: NfInstanceId = None       # lvdund
    nfType: NFType = None       # lvdund
    nfStatus: NFStatus = None       # lvdund
    heartBeatTimer: int = None
    plmnList: List[PlmnId] = []
    sNssais: List[Snssai] = []
    perPlmnSnssaiList: List[PlmnSnssai] = []
    nsiList: List[str] = []
    fqdn: Fqdn = None
    interPlmnFqdn: Fqdn = None
    ipv4Addresses: List[Ipv4Addr] = []
    ipv6Addresses: List[Ipv6Addr] = []
    allowedPlmns: List[PlmnId] = []
    allowedNfTypes: List[NFType] = []
    allowedNfDomains: List[str] = []
    allowedNssais: List[Snssai] = []
    priority: int = None
    capacity: int = None
    load: int = None
    locality: str = None
    udrInfo: UdrInfo = None
    udmInfo: UdmInfo = None
    ausfInfo: AusfInfo = None
    amfInfo: AmfInfo = None
    smfInfo: SmfInfo = None
    upfInfo: UpfInfo = None
    pcfInfo: PcfInfo = None
    bsfInfo: BsfInfo = None
    chfInfo: ChfInfo = None
    nrfInfo: NrfInfo = None
    customInfo: object = None
    recoveryTime: DateTime = None
    nfServicePersistence: bool = None
    nfServices: List[NFService] = []
    nfProfileChangesSupportInd: bool = None
    nfProfileChangesInd: bool = None
    defaultNotificationSubscriptions: List[DefaultNotificationSubscription] = []

    class Config:
        orm_mode = True
