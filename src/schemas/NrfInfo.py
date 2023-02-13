from typing import Dict

from src.schemas.common.NfInstanceId import NfInstanceId
from pydantic import BaseModel

from src.schemas.AmfInfo import AmfInfo
from src.schemas.AusfInfo import AusfInfo
from src.schemas.BsfInfo import BsfInfo
from src.schemas.ChfInfo import ChfInfo
from src.schemas.PcfInfo import PcfInfo
from src.schemas.SmfInfo import SmfInfo
from src.schemas.UdmInfo import UdmInfo
from src.schemas.UdrInfo import UdrInfo
from src.schemas.UpfInfo import UpfInfo


class NrfInfo(BaseModel):
    servedUdrInfo: Dict[NfInstanceId, UdrInfo] = None
    servedUdmInfo: Dict[NfInstanceId, UdmInfo] = None
    servedAusfInfo: Dict[NfInstanceId, AusfInfo] = None
    servedAmfInfo: Dict[NfInstanceId, AmfInfo] = None
    servedSmfInfo: Dict[NfInstanceId, SmfInfo] = None
    servedUpfInfo: Dict[NfInstanceId, UpfInfo] = None
    servedPcfInfo: Dict[NfInstanceId, PcfInfo] = None
    servedBsfInfo: Dict[NfInstanceId, BsfInfo] = None
    servedChfInfo: Dict[NfInstanceId, ChfInfo] = None
