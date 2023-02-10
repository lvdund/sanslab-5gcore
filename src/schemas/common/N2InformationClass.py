from enum import Enum


class N2InformationClass(str, Enum):
    sm = "SM"
    nrppa = "NRPPa"
    pws = "PWS"
    pws_bcal = "PWS-BCAL"
    pws_rf = "PWS-RF"
    ran = "RAN"
    v2x = "V2X"
