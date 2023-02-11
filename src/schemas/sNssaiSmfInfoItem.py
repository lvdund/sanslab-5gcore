from typing import List

from common.Snssai import Snssai
from pydantic import BaseModel

from schemas.DnnSmfInfoItem import DnnSmfInfoItem


class sNssaiSmfInfoItem(BaseModel):  # noqa: N801
    sNssai: Snssai
    dnnSmfInfoList: List[DnnSmfInfoItem]
