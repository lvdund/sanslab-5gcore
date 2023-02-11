from enum import Enum


class NotificationEventType(Enum):
    NF_REGISTERED = "NF_REGISTERED"
    NF_DEREGISTERED = "NF_DEREGISTERED"
    NF_PROFILE_CHANGED = "NF_PROFILE_CHANGED"
