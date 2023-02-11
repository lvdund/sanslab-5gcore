from common.NfInstanceId import NfInstanceId
from common.PlmnId import PlmnId
from pydantic import BaseModel

from schemas.GrantType import GrantType
from schemas.NFType import NFType


class AccessTokenReq(BaseModel):
    grant_type: GrantType
    nfInstanceId: NfInstanceId
    nfType: NFType = None
    targetNfType: NFType = None
    scope: str = None
    targetNfInstanceId: NfInstanceId = None
    requesterPlmn: PlmnId = None
    targetPlmn: PlmnId = None
