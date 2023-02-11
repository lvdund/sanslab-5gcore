from typing import List

from common.DateTime import DateTime
from common.Ipv4Addr import Ipv4Addr
from common.Ipv6Addr import Ipv6Addr
from common.NfInstanceId import NfInstanceId
from common.PlmnId import PlmnId
from common.Snssai import Snssai
from pydantic import BaseModel

from schemas.AmfInfo import AmfInfo
from schemas.AusfInfo import AusfInfo
from schemas.BsfInfo import BsfInfo
from schemas.ChfInfo import ChfInfo
from schemas.DefaultNotificationSubscription import DefaultNotificationSubscription
from schemas.Fqdn import Fqdn
from schemas.NFService import NFService
from schemas.NFStatus import NFStatus
from schemas.NFType import NFType
from schemas.NrfInfo import NrfInfo
from schemas.PcfInfo import PcfInfo
from schemas.PlmnSnssai import PlmnSnssai
from schemas.SmfInfo import SmfInfo
from schemas.UdmInfo import UdmInfo
from schemas.UdrInfo import UdrInfo
from schemas.UpfInfo import UpfInfo


class NFProfile(BaseModel):
    nfInstanceID: NfInstanceId
    nfType: NFType
    nfStatus: NFStatus
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
