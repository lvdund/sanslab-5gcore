
from typing import Dict, List

from src.schemas.common.Uri import Uri
from pydantic import BaseModel

from src.schemas.NFProfile import NFProfile
from src.schemas.NotificationEventType import NotificationEventType


class NotificationData(BaseModel):
    event: NotificationEventType
    nfInstanceUri: Uri
    nfProfile: NFProfile
    profileChanges: List[Dict] = []
