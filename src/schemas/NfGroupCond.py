
from common.NfGroupId import NfGroupId
from pydantic import BaseModel


class NfGroupCond(BaseModel):
    nfType: str
    nfGroupId: NfGroupId

    class Config:
        extra = "forbid"
