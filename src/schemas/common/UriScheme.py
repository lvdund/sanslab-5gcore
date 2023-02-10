from enum import Enum


class UriScheme(Enum):
    http = "http"
    https = "https"
    add = "ADD"
    move = "MOVE"
    remove = "REMOVE"
    replace = "REPLACE"
