# from dataclasses import dataclass, field

# #nullnftype
# Nullnftype = ( 'NRF','UDM','AMF','SMF','AUSF','NEF','PCF','SMSF','NSSF','UDR','LMF','GMLC','5G_EIR','SEPP','UPF','N3IWF','AF','UDSF','BSF','CHF','NWDAF')

# #AmfName

# #ChangeType
# ChangeType = ('ADD','MOVE','REMOVE','REPLACE')

# #ChangeItem
# @dataclass
# class ChangeItem:
#     op: str = ''
#     path: str = ''
#     # from: str = '' #fromChangeItem = form
#     origValue: any = ''
#     newValue: any = ''
# #N2InformationClass
# N2informationClass = ('SM','NRPPa','PWS','PWS-BCAL','PWS-RF','RAN')

# #N1MessageClass
# N1MessageClass = ('5GMM','SM','LPP','SMS','UPDP')

# #Ipv6Prefix

# #DiameterIdentity

# #Dnai

# #Dnn

# #AccessType
# AccessType = ('3GPP_ACCESS', 'NON_3GPP_ACCESS')


# #Tai
# @dataclass
# class PlmnId:
#     mcc: str = ''
#     mnc: str = ''

# @dataclass
# class Tai:
#     plmnId: PlmnId = PlmnId()
#     tac: str = ''

# #NfgroupId

# #AmfId

# #Guami
# @dataclass
# class Guami:
#     plmnId: PlmnId = PlmnId()
#     amfId: str = ''

# #SupportedFeatures

# #UriScheme
# UriScheme = ('http','https')

# #DateTime

# # #Ipv6Addr
# # @dataclass
# # class Ipv6Addr:
# #     ipv6Addr: str = ''

# # #Ippv4Addr
# # @dataclass
# # class Ipv4Addr:
# #     ipv4Addr: str = ''
# #Snssai
# @dataclass
# class Snssai:
#     sst: int = 0
#     sd: str = ''

# #Mnc

# #Mcc

# #PlmnId

# #PatchOperation
# PatchOperation = ('add','copy','move','remove','replace','test')

# #PatchItem
# @dataclass
# class PatchItem:
#     op: PatchOperation
#     path: str = ''
#     _from: str = ''
#     value: any = '' 

# #NfInstanceId

# #InvalidParam
# @dataclass
# class InvalidParam:
#     param: str = ''
#     reason: str = ''

# #ProblemDetails
# @dataclass
# class ProblemDetails:
#     type: str = ''
#     title: str = ''
#     status: int = 0
#     detail: str = ''
#     instance: str = ''
#     cause: str = ''
#     invalidParams: InvalidParam = InvalidParam()

# #Uri

# #Link
# @dataclass
# class Link:
#     href: str = ''

# # #LinksValueSchema 
# # @dataclass
# # class LinksValueSchema:
# #     oneOf: list[Link] = field(default_factory=list)

# #NrfInfo
# @dataclass
# class SupiRange:
#     start: str = ''
#     end: str = ''
#     pattern: str = ''

# @dataclass
# class IdentityRange:
#     start: str = ''
#     end: str = ''
#     pattern: str = ''

# DataSetId = ('SUBSCRIPTION','POLICY','EXPOSURE','APPLICATION')
# DataSetId = ('SUBSCRIPTION', 'POLICY', 'EXPOSURE', 'APPLICATION')

# @dataclass
# class UdrInfo:
#     groupId: str = ''
#     supiRanges: list[SupiRange] = field(default_factory=list)
#     gpsiRanges: list[IdentityRange] = field(default_factory=list)
#     externalGroupIdentifiersRanges: list[IdentityRange] = field(default_factory=list)
#     supportedDataSets: list[DataSetId] = field(default_factory=list)

# @dataclass
# class UdmInfo:
#     groupId: str = ''
#     supiRanges: list[SupiRange] = field(default_factory=list)
#     gpsiRanges: list[IdentityRange] = field(default_factory=list)
#     routingIndicators: list[str] = field(default_factory=list)

# @dataclass
# class AusfInfo:
#     groupId: str = ''
#     supiRanges: list[SupiRange] = field(default_factory=list)
#     routingIndicators: list[str] = field(default_factory=list)

# @dataclass 
# class Guami:
#     plmnId: PlmnId = PlmnId()
#     amfId: str = ''

# #TacRange
# @dataclass
# class TacRange:
#     start: str = ''
#     end: str = ''
#     pattern: str = ''

# #TaiRange
# @dataclass 
# class TaiRange:
#     plmnId: PlmnId = PlmnId()
#     tacRangeList: list[TacRange] = field(default_factory=list)

# Ipv4Addr = ''
# Ipv6Addr = ''
# #N2InterfaceAmfInfo
# @dataclass
# class N2InterfaceAmfInfo:
#     ipv4EndpointAddress: list[Ipv4Addr] = field(default_factory=list)
#     ipv6EndpointAddress: list[Ipv6Addr] = field(default_factory=list)
#     amfName: str = ''

# @dataclass
# class AmfInfo:
#     amfSetId: str = ''
#     amdRegionId: str = ''
#     guamiList: list[Guami] = field(default_factory=list)
#     taiList: list[Tai] = field(default_factory=list)
#     taiRangeList: list[TaiRange] = field(default_factory=list)
#     n2InterfaceAmfInfo: N2InterfaceAmfInfo = N2InterfaceAmfInfo()

# @dataclass
# class Snssai:
#     sst: int = 0
#     sd: str = ''

# @dataclass
# class DnnSmfInfoItem:
#     dnn: str = ''

# @dataclass
# class SnssaiSmfInfoItem:
#     sNssai: Snssai = Snssai()
#     dnnSmfInfoList: list[DnnSmfInfoItem] = field(default_factory=list)

# @dataclass
# class SmfInfo:
#     sNssaiSmfInfoList: list[SnssaiSmfInfoItem] = field(default_factory=list)
#     taiList: list[Tai] = field(default_factory=list)
#     taiRangeList: list[TaiRange] = field(default_factory=list)
#     pgwFqdn: str = ''
#     accessType: list[AccessType] = field(default_factory=list)

# @dataclass
# class Snssai:
#     sst: int = 0
#     sd: str = ''

# @dataclass
# class Dnai:
#     dnai: str = ''

# @dataclass
# class DnnUpfInfoItem:
#     dnn: str = ''
#     dnaiList: list[Dnai] = field(default_factory=list)


# @dataclass
# class SnssaiUpfInfoItem:
#     sNssai: Snssai = Snssai()
#     dnnUpfInfoList: list[DnnUpfInfoItem] =  field(default_factory=list)

# smfServingAreaItem: str = ''
# UPInterfaceType = ('N3', 'N6', 'N9')

# @dataclass
# class InterfaceUpfInfoList:
#     interfaceType: UPInterfaceType
#     ipv4EndpointAddresses: Ipv4Addr
#     ipv6EndpointAddresses: Ipv6Addr
#     endpointFqdn: str = ''
#     networkInstance: str = ''

# @dataclass
# class UpfInfo:
#     sNssaiUpfInforList:  list[SnssaiUpfInfoItem] = field(default_factory=list)
#     smfServingArea: list[smfServingAreaItem] = field(default_factory=list)
#     interfaceUpfInfoList: list[InterfaceUpfInfoList] = field(default_factory=list)
#     iwkEpsInd: bool = False

# @dataclass
# class Dnn:
#     dnn: str = ''
# @dataclass 
# class PcfInfo:
#     dnnList: list[Dnn] = field(default_factory=list)
#     supiRanges: list[SupiRange] = field(default_factory=list)
#     rxDiamHost: str = ''
#     rxDiamRealm: str = ''

# ipDomainItem: str = ''

# @dataclass
# class Ipv4AddressRange:
#     start: str = ''
#     end: str = ''
# Ipv6Prefix: str = ''
# @dataclass
# class Ipv6PrefixRange:
#     start: list[Ipv6Prefix] = field(default_factory=list)
#     end: list[Ipv6Prefix] = field(default_factory=list)

# @dataclass
# class BsfInfo:
#     dnnList: list[Dnn] = field(default_factory=list)
#     ipDomainList: list[ipDomainItem] = field(default_factory=list)
#     ipv4AddressRanges: list[Ipv4AddressRange] = field(default_factory=list)
#     Ipv6PrefixRanges: list[Ipv6PrefixRange] = field(default_factory=list)

# #PlmnRange
# @dataclass
# class PlmnRange:
#     start: str = ''
#     end: str = ''
#     pattern: str = ''

# @dataclass
# class ChfInfo:
#     supiRangeList: list[SupiRange] = field(default_factory=list)
#     gpsiRangeList: list[IdentityRange] = field(default_factory=list)
#     plmnRangeList: list[PlmnRange] = field(default_factory=list)

# @dataclass
# class NrfInfo:
#     servedUdrInfo: list[UdrInfo] = field(default_factory=list)
#     servedUdmInfo: list[UdmInfo] = field(default_factory=list)
#     servedAusfInfo: list[AusfInfo] = field(default_factory=list)
#     servedAmfInfo: list[AmfInfo] = field(default_factory=list)
#     servedSmfInfo: list[SmfInfo] = field(default_factory=list)
#     servedUpfInfo: list[UpfInfo] = field(default_factory=list)
#     servedPcfInfo: list[PcfInfo] = field(default_factory=list)
#     servedBsfInfo: list[BsfInfo] = field(default_factory=list)
#     servedChfInfo: list[ChfInfo] = field(default_factory=list)

# #NFServiceStatus
# NFServiceStatus = ('REGISTERED', 'SUSPENDED')

# #ServiceName
# ServiceName = ('nnrf-nfm', 'nnrf-disc', 'nudm-sdm', 'nudm-uecm', 'nudm-ueau', 'nudm-ee', 'nudm-pp', 'namf-comm', 'namf-evts', 'namf-mt', 'namf-loc', 'nsmf-pdusession', 'nsmf-event-exposure', 'nausf-auth', 'nausf-sorprotection', 'nnef-pfdmanagement', 'npcf-am-policy-control', 'npcf-smpolicycontrol', 'npcf-policyauthorization', 'npcf-bdtpolicycontrol', 'npcf-eventexposure', 'npcf-ue-policy-control', 'nsmsf-sms', 'nnssf-nsselection', 'nnssf-nssaiavailability', 'nudr-dr', 'nlmf-loc', 'n5g-eir-eic', 'nbsf-management', 'nchf-spendinglimitcontrol', 'nchf-convergedcharging', 'nnwdaf-eventssubscription', 'nnwdaf-analyticsinfo')

# #NFServiceVersion
# @dataclass
# class NFServiceVersion:
#     apiVersionInUri: str = ''
#     apiFullVersion: str = ''
#     expiry: str = ''

# #NFStatus
# NFStatus = ('REGISTERED', 'SUSPENDED')

# NotificationEventType = ('NF_REGISTERED', 'NF_DEREGISTERED', 'NF_PROFILE_CHANGED')

# NFType = ('NRF','UDM','AMF','SMF','AUSF','NEF','PCF','SMSF','NSSF','UDR','LMF','GMLC','5G_EIR','SEPP','UPF','N3IWF','AF','UDSF','BSF','CHF','NWDAF')
# NsiItem: str = ''
# AllowedNfDomains: str = ''

# ServiceName = ('nnrf-nfm','nnrf-disc','nudm-sdm','nudm-uecm','nudm-ueau','nudm-ee','nudm-pp','namf-comm','namf-evts','namf-mt','namf-loc','nsmf-pdusession','nsmf-event-exposure','nausf-auth','nausf-sorprotection','nnef-pfdmanagement','npcf-am-policy-control','npcf-smpolicycontrol','npcf-policyauthorization','npcf-bdtpolicycontrol','npcf-eventexposure','npcf-ue-policy-control','nsmsf-sms','nnssf-nsselection','nnssf-nssaiavailability','nudr-dr','nlmf-loc','n5g-eir-eic','nbsf-management','nchf-spendinglimitcontrol','nchf-convergedcharging','nnwdaf-eventssubscription','nnwdaf-analyticsinfo')
# TransportProtocol = ('TCP')
# NotificationType = ('N1_MESSAGES', 'N2_INFORMATION', 'LOCATION_NOTIFICATION', 'DATA_REMOVAL_NOTIFICATION', 'DATA_CHANGE_NOTIFICATION')
# N1MessageClass = ('5GMM', 'SM', 'LPP', 'SMS', 'UPDP')
# N2InformationClass = ('SM', 'NRPPa', 'PWS', 'PWS-BCAL', 'PWS-RF', 'RAN ')
# @dataclass
# class IpEndPoint:
#     ipv4Address: str = ''
#     ipv6Address: str = ''
#     transport: str = ''
#     port: int = 0

# @dataclass
# class DefaultNotificationSubscription:
#     notificationType: NotificationType
#     callbackUri: str = ''
#     n1MessageClass: str = ''
#     n2InformationClass: str = ''

# AllowedNfDomain: str = ''

# @dataclass
# class ChfServiceInfo:
#     primaryChfServiceInstance: str = ''
#     secondaryChfServiceInstance: str = ''
#     nots: str = ''
# @dataclass
# class NFService:
#     serviceInstanceId: str = ''
#     serviceName: str = ''
#     versions: list[NFServiceVersion] = field(default_factory=list)
#     scheme: str = ''
#     nfServiceStatus: str = ''
#     fqdn: str = ''
#     interPlmnFqdn: str = ''
#     ipEndPoints: list[IpEndPoint] = field(default_factory=list)
#     apiPrefix: str = ''
#     defaultNotificationSubscriptions: list[DefaultNotificationSubscription] = field(default_factory=list)
#     allowedPlmns: list[PlmnId] = field(default_factory=list)
#     allowedNfTypes: list[NFType] = field(default_factory=list)
#     allowedNfDomains: list[AllowedNfDomain] = field(default_factory=list)
#     allowedNssais: list[Snssai] = field(default_factory=list)
#     priority: int = 0
#     capacity: int = 0
#     load: int = 0
#     recoveryTime: str = ''
#     chfServiceInfo: ChfServiceInfo = ChfServiceInfo()
#     supportedFeatures: str = ''


# @dataclass
# class NfProfile:
#     nfInstanceId: str = ''
#     nfType: str = ''
#     nFStatus: str = ''
#     plmnList: list[PlmnId] = field(default_factory=list)
#     sNssais: list[Snssai] = field(default_factory=list)
#     nsiList: list[NsiItem] = field(default_factory=list)
#     fqdn: str = ''
#     interPlmnFqdn: str = ''
#     ipv4Addresses: list[Ipv4Addr] =  field(default_factory=list)
#     ipv6Addresses: list[Ipv6Addr] =  field(default_factory=list)
#     allowedPlmns: list[PlmnId] = field(default_factory=list)
#     allowedNfTypes: list[NFType] = field(default_factory=list)
#     allowedNfDomains: list[AllowedNfDomains] = field(default_factory=list)
#     allowedNssais: list[Snssai] = field(default_factory=list)
#     priority: int = 0
#     capacity: int = 0
#     load: int  = 0
#     locality: str = ''
#     udrInfo: UdrInfo = UdrInfo()
#     udmInfo: UdmInfo = UdmInfo()
#     ausfInfo: AusfInfo = AusfInfo()
#     amfInfo: AmfInfo = AmfInfo()
#     smfInfo: SmfInfo = SmfInfo()
#     upfInfo: UpfInfo = UpfInfo()
#     pcfInfo: PcfInfo = PcfInfo()
#     bsfInfo: BsfInfo = BsfInfo()
#     chfInfo: ChfInfo = ChfInfo()
#     nrfInfo: NrfInfo = NrfInfo()
#     customInfo: str = ''
#     recoveryTime: str = ''
#     nfServicePersistence: bool = False
#     nfService: list[NFService] = field(default_factory=list)
#     anyOf: list[str] = ''
#     nots: str = ''



# #NotificationData
# @dataclass
# class NotificationData:
#     event: NotificationEventType
#     nfInstanceUri: str = ''
#     nfProfile: NfProfile = NfProfile()
#     profileChanges: ChangeItem = ChangeItem()
#     anyOf = ''

# @dataclass
# class NotifCondition:
#     monitoredAttributes: list[str] = field(default_factory=list)
#     unmonitoredAttributes: list[str] = field(default_factory=list)

# @dataclass
# class NfGroupCond:
#     nfType = ('UDM', 'AUSF', 'UDR')
#     nfGroupId: str = ''

# @dataclass
# class NetworkSliceCond:
#     snssaiList: list[Snssai] = field(default_factory=list)
#     nsiList: list[str] = field(default_factory=list)

# @dataclass
# class GuamiListCond:
#     guamiList: list[Guami] = field(default_factory=list)

# @dataclass
# class AmfCond:
#     amfSerId: str = ''
#     amfRegionId: str = ''
#     anyOf = ''

# @dataclass
# class ServiceNameCond:
#     serviceName: ServiceName

# @dataclass
# class NfTypeCond:
#     nfType: NFType

# @dataclass
# class NFInstanceIdCond:
#     nfInstanceId: str = ''

# @dataclass
# class SubscriptionData:
#     nfStatusNotificationUri: str = ''
#     subscrCond: any = ''
#     subscriptionId: str = ''
#     validityTime: str = ''
#     reqNotifEvents: list[NotificationEventType] = field(default_factory=list)
#     plmnId: PlmnId = PlmnId()
#     notifCondition: NotifCondition = NotifCondition()
#     reqNfType: str = ''
#     reqNfFqdn: str = ''
