from dataclasses import dataclass

NFTypes = ( 'NRF', 'UDM', 'AMF', 'SMF', 'AUSF', 'NEF', 'PCF', 'SMSF', 'NSSF', 
           'UDR', 'LMF', 'GMLC', '5G_EIR', 'SEPP', 'UPF', 'N3IWF', 'AF', 'UDSF', 'BSF', 'CHF', 'NWDAF')

@dataclass
class PlmnId:
    mcc: str
    mnc: str