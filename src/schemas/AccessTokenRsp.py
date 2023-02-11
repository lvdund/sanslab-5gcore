from pydantic import BaseModel


class AccessTokenRsp(BaseModel):
    access_token: str
    token_type: str
    expires_in: int = None
    scope: str = None
