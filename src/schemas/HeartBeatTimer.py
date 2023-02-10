from pydantic import BaseModel
from src.schemas.NFStatus import NFStatus
from src.schemas.common.NfInstanceId import NfInstanceId

class Nf_heartBeat(BaseModel):
    nfInstanceId: NfInstanceId
    nfStatus: NFStatus
    updateTime: float

listNF_heartBeatTimer = []