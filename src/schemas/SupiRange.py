from pydantic import BaseModel


class SupiRange(BaseModel):
    start: str = None
    end: str = None
    pattern: str = None
