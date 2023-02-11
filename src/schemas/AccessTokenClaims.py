from datetime import datetime
from typing import List, Union

from common.NfInstanceId import NfInstanceId
from pydantic import BaseModel

from schemas.NFType import NFType


class AccessTokenClaims(BaseModel):
    iss: NfInstanceId
    sub: NfInstanceId
    aud: Union[NFType, List[NfInstanceId]]
    scope: str
    exp: datetime
