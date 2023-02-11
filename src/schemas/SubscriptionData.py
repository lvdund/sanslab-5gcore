from typing import List, Union

from common.DateTime import DateTime
from common.PlmnId import PlmnId
from common.Uri import Uri
from pydantic import BaseModel

from schemas.AmfCond import AmfCond
from schemas.Fqdn import Fqdn
from schemas.GuamiListCond import GuamiListCond
from schemas.NetworkSliceCond import NetworkSliceCond
from schemas.NfGroupCond import NfGroupCond
from schemas.NfInstanceIdCond import NfInstanceIdCond
from schemas.NFType import NFType
from schemas.NfTypeCond import NfTypeCond
from schemas.NotifCondition import NotifCondition
from schemas.NotificationEventType import NotificationEventType
from schemas.ServiceNameCond import ServiceNameCond


class SubscriptionData(BaseModel):
    nfStatusNotificationUri: Uri
    subscrCond: Union[
        NfInstanceIdCond,
        NfTypeCond,
        ServiceNameCond,
        AmfCond,
        GuamiListCond,
        NetworkSliceCond,
        NfGroupCond,
    ] = None
    subscriptionId: str = None
    validityTime: DateTime = None
    reqNotifEvents: List[NotificationEventType] = []
    reqNfType: NFType = None
    reqNfFqdn: Fqdn = None
    plmnId: PlmnId = None
    notifCondition: NotifCondition = None

    class Config:
        orm_mode = True
