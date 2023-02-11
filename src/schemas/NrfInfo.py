from typing import Dict

from common.NfInstanceId import NfInstanceId
from pydantic import BaseModel

from schemas.AmfInfo import AmfInfo
from schemas.AusfInfo import AusfInfo
from schemas.BsfInfo import BsfInfo
from schemas.ChfInfo import ChfInfo
from schemas.PcfInfo import PcfInfo
from schemas.SmfInfo import SmfInfo
from schemas.UdmInfo import UdmInfo
from schemas.UdrInfo import UdrInfo
from schemas.UpfInfo import UpfInfo


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
