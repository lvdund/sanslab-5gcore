from pydantic import BaseModel


class IdentityRange(BaseModel):
    start: str = None
    end: str = None
    pattern: str = None
