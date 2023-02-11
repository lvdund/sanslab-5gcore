from enum import Enum


class NFServiceStatus(str, Enum):
    registered = "REGISTERED"
    suspended = "SUSPENDED"
    undiscoverable = "UNDISCOVERABLE"
