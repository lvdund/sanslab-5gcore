from common.DateTime import DateTime
from pydantic import BaseModel


class NFServiceVersion(BaseModel):
    apiVersionInUri: str
    apiFullVersion: str
    expiry: DateTime = None
