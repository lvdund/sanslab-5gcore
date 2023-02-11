from typing import List

from pydantic import BaseModel


class NotifCondition(BaseModel):  # noqa: N801
    monitoredAttributes: List[str] = []
    unmonitoredAttributes: List[str] = []
