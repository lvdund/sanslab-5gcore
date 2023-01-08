from dataclasses import dataclass
from Services.schemas import *

Grant_type = ( 'client_credentials')
Error = ( 'invalid_request', 'invalid_client', 'invalid_grant', 'unauthorized_client', 'unsupported_grant_type', 'invalid_scope')

@dataclass
class AccessTokenReq:
    grant_type: str
    nfInstanceId: str
    nfType: str
    targetNfType: str
    scope: str
    targetNfInstanceId: str
    requesterPlmn: PlmnId
    targetPlmn: PlmnId

@dataclass
class AccessTokenRsp:
    access_token: str
    token_type: int
    expires_in: str
    scope: str

@dataclass
class AccessTokenClaims:
    issuer: str
    subject: int
    audience: any
    scope: str
    expiration: int

@dataclass
class AccessTokenErr:
    error: str
    error_description: int
    error_uri: str
