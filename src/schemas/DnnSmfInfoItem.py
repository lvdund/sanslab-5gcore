from src.schemas.common.Dnn import Dnn
from pydantic import BaseModel


class DnnSmfInfoItem(BaseModel):
    dnn: Dnn
