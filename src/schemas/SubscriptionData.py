from typing import List, Union

from src.schemas.common.DateTime import DateTime
from src.schemas.common.PlmnId import PlmnId
from src.schemas.common.Uri import Uri
from pydantic import BaseModel

from src.schemas.AmfCond import AmfCond
from src.schemas.Fqdn import Fqdn
from src.schemas.GuamiListCond import GuamiListCond
from src.schemas.NetworkSliceCond import NetworkSliceCond
from src.schemas.NfGroupCond import NfGroupCond
from src.schemas.NfInstanceIdCond import NfInstanceIdCond
from src.schemas.NFType import NFType
from src.schemas.NfTypeCond import NfTypeCond
from src.schemas.NotifCondition import NotifCondition
from src.schemas.NotificationEventType import NotificationEventType
from src.schemas.ServiceNameCond import ServiceNameCond


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
