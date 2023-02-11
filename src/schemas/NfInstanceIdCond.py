from common.NfInstanceId import NfInstanceId
from pydantic import BaseModel


class NfInstanceIdCond(BaseModel):
    nfInstanceId: NfInstanceId
