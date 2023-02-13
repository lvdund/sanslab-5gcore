from src.schemas.common.N1MessageClass import N1MessageClass
from src.schemas.common.N2InformationClass import N2InformationClass
from src.schemas.common.Uri import Uri
from pydantic import BaseModel

from src.schemas.NotificationType import NotificationType


class DefaultNotificationSubscription(BaseModel):
    notificationType: NotificationType
    callbackUri: Uri
    n1MessageClass: N1MessageClass = None
    n2InformationClass: N2InformationClass = None
