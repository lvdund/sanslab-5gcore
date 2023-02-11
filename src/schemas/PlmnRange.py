from pydantic import BaseModel


class PlmnRange(BaseModel):
    start: str = None
    end: str = None
    pattern: str = None
