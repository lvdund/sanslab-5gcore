from enum import Enum


class NotificationType(str, Enum):
    n1_messages = "N1_MESSAGES"
    n2_information = "N2_INFORMATION"
    location_notification = "LOCATION_NOTIFICATION"
    data_removal_notification = "DATA_REMOVAL_NOTIFICATION"
    data_change_notification = "DATA_CHANGE_NOTIFICATION"
