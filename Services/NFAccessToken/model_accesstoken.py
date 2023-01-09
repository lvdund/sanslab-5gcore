from dataclasses import dataclass
from Services.model import *

Grant_type = ( 'client_credentials')
Error = ( 'invalid_request', 'invalid_client', 'invalid_grant', 'unauthorized_client', 'unsupported_grant_type', 'invalid_scope')

@dataclass
class AccessTokenReq:
    grant_type: str = ''
    nfInstanceId: str = ''
    nfType: str = ''
    targetNfType: str = ''
    scope: str = ''
    targetNfInstanceId: str = ''
    requesterPlmn: PlmnId = PlmnId('', '')
    targetPlmn: PlmnId = PlmnId('', '')

@dataclass
class AccessTokenRsp:
    access_token: str = ''
    token_type: int = 0
    expires_in: str = ''
    scope: str = ''

@dataclass
class AccessTokenClaims:
    issuer: str = ''
    subject: int = 0
    audience: any = ''
    scope: str = ''
    expiration: int = 0

@dataclass
class AccessTokenErr:
    error: str = ''
    error_description: int = 0
    error_uri: str = ''
