from typing import List

from src.schemas.common.Snssai import Snssai
from pydantic import BaseModel

from src.schemas.DnnSmfInfoItem import DnnSmfInfoItem


class sNssaiSmfInfoItem(BaseModel):  # noqa: N801
    sNssai: Snssai
    dnnSmfInfoList: List[DnnSmfInfoItem]
