
from typing import Dict, List

from common.Uri import Uri
from pydantic import BaseModel

from schemas.NFProfile import NFProfile
from schemas.NotificationEventType import NotificationEventType


class NotificationData(BaseModel):
    event: NotificationEventType
    nfInstanceUri: Uri
    nfProfile: NFProfile = None
    profileChanges: List[Dict] = []
