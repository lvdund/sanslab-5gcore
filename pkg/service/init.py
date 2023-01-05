from typing import NamedTuple

class NRF(NamedTuple):
    KeyLogPath: str

class Commands(NamedTuple):
    config: str
    nrf: NRF

