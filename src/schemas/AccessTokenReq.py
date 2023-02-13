from src.schemas.common.NfInstanceId import NfInstanceId
from src.schemas.common.PlmnId import PlmnId
from pydantic import BaseModel

from src.schemas.GrantType import GrantType
from src.schemas.NFType import NFType


class AccessTokenReq(BaseModel):
    grant_type: GrantType
    nfInstanceId: NfInstanceId
    nfType: NFType = None
    targetNfType: NFType = None
    scope: str = None
    targetNfInstanceId: NfInstanceId = None
    requesterPlmn: PlmnId = None
    targetPlmn: PlmnId = None
