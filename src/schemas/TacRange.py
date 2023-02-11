from pydantic import BaseModel


class TacRange(BaseModel):
    start: str = None
    end: str = None
    pattern: str = None
