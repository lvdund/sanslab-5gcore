from common.N1MessageClass import N1MessageClass
from common.N2InformationClass import N2InformationClass
from common.Uri import Uri
from pydantic import BaseModel

from schemas.NotificationType import NotificationType


class DefaultNotificationSubscription(BaseModel):
    notificationType: NotificationType
    callbackUri: Uri
    n1MessageClass: N1MessageClass = None
    n2InformationClass: N2InformationClass = None
