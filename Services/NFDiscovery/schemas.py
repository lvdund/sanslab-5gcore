from dataclasses import dataclass, field
from Services.schemas import *

NfStatus = ( 'REGISTERED', 'SUSPENDED')
DataSetId = ( 'SUBSCRIPTION', 'POLICY', 'EXPOSURE', 'APPLICATION')
AccessType = ( '3GPP_ACCESS', 'NON_3GPP_ACCESS')

@dataclass
class Snssai:
    stt: int
    sd: int

@dataclass
class SupiRange:
    start: str
    end: str
    pattern: str

@dataclass
class IdentityRange:
    start: str
    end: str
    pattern: str

@dataclass
class UdrInfo:
    groupId: str
    supportedDataSets: str
    supiRanges: list[SupiRange] = field(default_factory=list)
    gpsiRanges: list[IdentityRange] = field(default_factory=list)
    externalGroupIdentifiersRanges: list[IdentityRange] = field(default_factory=list)

@dataclass
class UdmInfo:
    groupId: str
    supiRanges: list[SupiRange] = field(default_factory=list)
    gpsiRanges: list[IdentityRange] = field(default_factory=list)
    externalGroupIdentifiersRanges: list[IdentityRange] = field(default_factory=list)
    routingIndicators: list[str] = field(default_factory=list)

@dataclass
class AusfInfo:
    groupId: str
    supiRanges: list[SupiRange] = field(default_factory=list)
    routingIndicators: list[str] = field(default_factory=list)

@dataclass
class Guami:
    plmnId: PlmnId
    amfId: str

@dataclass
class Tai:
    plmnId: PlmnId
    tac: str

@dataclass
class TacRange:
    start: str
    end: str
    pattern: str

@dataclass
class TaiRange:
    plmnId: PlmnId
    tacRangeList: TacRange

@dataclass
class N2InterfaceAmfInfo:
    amfName: str
    ipv4EndpointAddress: list(str) = field(default_factory=list)
    ipv6EndpointAddress: list(str) = field(default_factory=list)

@dataclass
class AmfInfo:
    amfSetId: str
    amfRegionId: str
    n2InterfaceAmfInfo: N2InterfaceAmfInfo
    guamiList: list(Guami) = field(default_factory=list)
    taiList: list(Tai) = field(default_factory=list)
    taiRangeList: list(TaiRange) = field(default_factory=list)
    backupInfoAmfFailure: list[Guami] = field(default_factory=list)

@dataclass
class DnnSmfInfoItem:
    dnn: str
    
@dataclass
class SnssaiSmfInfoItem:
    sNssai: Snssai
    dnnSmfInfoList: list[DnnSmfInfoItem] = field(default_factory=list)

@dataclass
class SmfInfo:
    pgwFqdn: str
    accessType: list[str] = field(default_factory=list)
    sNssaiSmfInfoList: list[SnssaiSmfInfoItem] = field(default_factory=list)
    taiList: list[Tai] = field(default_factory=list)
    taiRangeList: list[TaiRange] = field(default_factory=list)

@dataclass
class DnaiList:
    Dnai: list[str] = field(default_factory=list)

@dataclass
class DnnUpfInfoItem:
    dnn: str
    dnaiList: list[DnnSmfInfoItem] = field(default_factory=list)

@dataclass
class SnssaiUpfInfoItem:
    sNssai: list[Snssai] = field(default_factory=list)
    dnnSmfInfoIList: list(DnnSmfInfoItem) = field(default_factory=list)

UPInterfaceType = ( 'N3', 'N6', 'N9')

@dataclass
class InterfaceUpfInfoItem:
    interfaceType: str
    endpointFqdn: str
    networkInstance: str
    ipv4EndpointAddresses: list(str) = field(default_factory=list)
    ipv4EndpointAddresses: list(str) = field(default_factory=list)
    
@dataclass
class UpfInfo:
    sNssaiUpfInfoList: list(SnssaiSmfInfoItem) = field(default_factory=list)
    smfServingArea: list(str) = field(default_factory=list)
    interfaceUpfInfoList: list(InterfaceUpfInfoItem) = field(default_factory=list)
    iwkEpsInd: bool = True

@dataclass
class PcfInfo:
    rxDiamHost: str
    rxDiamRealm: str
    dnnList: list(str) = field(default_factory=list)
    supiRanges: list(SupiRange) = field(default_factory=list)

@dataclass
class Ipv4AddressRange:
    start: str
    end: str

@dataclass
class Ipv6PrefixRange:
    start: str
    end: str

@dataclass
class BsfInfo:
    dnnList: list(str) = field(default_factory=list)
    ipDomainList: list(str) = field(default_factory=list)
    ipv4AddressRanges: list(Ipv4AddressRange) = field(default_factory=list)
    ipv6PrefixRanges: list(Ipv6PrefixRange) = field(default_factory=list)

@dataclass
class PlmnRange:
    start: str
    end: str
    pattern: str    

@dataclass
class ChfInfo:
    supiRangeList: list(SupiRange) = field(default_factory=list)
    gpsiRangeList: list(IdentityRange) = field(default_factory=list)
    plmnRangeList: list(PlmnRange) = field(default_factory=list)

ServiceName = ( 'nnrf-nfm', 'nnrf-disc', 'nudm-sdm', 'nudm-uecm', 'nudm-ueau', 
               'nudm-ee', 'nudm-pp', 'namf-comm', 'namf-evts', 'namf-mt', 'namf-loc', 
               'nsmf-pdusession', 'nsmf-event-exposure', 'nausf-auth', 'nausf-sorprotection', 
               'nnef-pfdmanagement', 'npcf-am-policy-control', 'npcf-smpolicycontrol', 
               'npcf-policyauthorization', 'npcf-bdtpolicycontrol', 'npcf-eventexposure', 
               'npcf-ue-policy-control', 'nsmsf-sms', 'nnssf-nsselection', 'nnssf-nssaiavailability', 
               'nudr-dr', 'nlmf-loc', 'n5g-eir-eic', 'nbsf-management', 'nchf-spendinglimitcontrol', 
               'nchf-convergedcharging', 'nnwdaf-eventssubscription', 'nnwdaf-analyticsinfo')

UriScheme = ( 'http', 'https')
NFServiceStatus = ( 'REGISTERED', 'SUSPENDED')
TransportProtocol = ( 'TCP')
NotificationType = ('N1_MESSAGES', 'N2_INFORMATION', 'LOCATION_NOTIFICATION', 
                    'DATA_REMOVAL_NOTIFICATION', 'DATA_CHANGE_NOTIFICATION')
N1MessageClass = ('5GMM', 'SM', 'LPP', 'SMS', 'UPDP')
N2InformationClass = ('SM', 'NRPPa', 'PWS', 'PWS-BCAL', 'PWS-RF', 'RAN')

@dataclass
class NFServiceVersion:
    apiVersionInUri: str
    apiFullVersion: str
    expiry: str

@dataclass
class IpEndPoint:
    ipv4Address: str
    ipv6Address: str
    transport: str
    port: int

@dataclass
class DefaultNotificationSubscription:
    notificationType: str
    callbackUri: str
    n1MessageClass: str
    n2InformationClass: str

@dataclass
class ChfServiceInfo:
    primaryChfServiceInstance: str
    secondaryChfServiceInstance: str

@dataclass
class DefaultNotificationSubscription:
    notificationType: str
    callbackUri: str
    n1MessageClass: str
    n2InformationClass: str
    
@dataclass
class NFService:
    serviceInstanceId: str
    serviceName: str
    scheme: str
    nfServiceStatus: str
    fqdn: str
    apiPrefix: str
    capacity: int
    load: int
    priority: int
    recoveryTime: str
    supportedFeatures: str
    chfServiceInfo: ChfServiceInfo
    versions: list(NFServiceVersion) = field(default_factory=list)
    ipEndPoints: list(IpEndPoint) = field(default_factory=list)
    defaultNotificationSubscriptions: list(DefaultNotificationSubscription) = field(default_factory=list)

@dataclass
class NFProfile:
    customInfo: any
    nfInstanceId: str
    nfType: str
    nfStatus: str
    fqdn: str
    capacity: str
    load: int
    locality: str
    priority: int
    recoveryTime: str
    nfServicePersistence: bool = False
    plmnList: list(PlmnId) = field(default_factory=list)
    sNssais: list(Snssai) = field(default_factory=list)
    nsiList: list(str) = field(default_factory=list)
    ipv4Addresses: list(str) = field(default_factory=list)
    ipv6Addresses: list(str) = field(default_factory=list)
    udrInfo: list(UdrInfo) = field(default_factory=list)
    udmInfo: list(UdmInfo) = field(default_factory=list)
    ausfInfo: list(AusfInfo) = field(default_factory=list)
    amfInfo: list(AmfInfo) = field(default_factory=list)
    smfInfo: list(SmfInfo) = field(default_factory=list)
    upfInfo: list(UpfInfo) = field(default_factory=list)
    pcfInfo: list(PcfInfo) = field(default_factory=list)
    bsfInfo: list(BsfInfo) = field(default_factory=list)
    chfInfo: list(ChfInfo) = field(default_factory=list)
    nfServices: list(NFService) = field(default_factory=list)

@dataclass
class SearchResult:
    validityPeriod: int
    nfInstances: NFProfile