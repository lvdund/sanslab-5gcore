from pydantic import BaseModel

from .Snssai import Snssai


class ConfiguredSnssai(BaseModel):
    configuredSnssai: Snssai
    mappedHomeSnssai: Snssai = None
