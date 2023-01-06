from model.mongoapi import SetMongoDB
from pkg.factory.factory import CheckConfigVersion
from pkg.factory.factory import NrfConfig
from pkg.factory.config import Config

class NRF:
    def __init__(self, KeyLogPath):
        self.KeyLogPath = KeyLogPath
    
    def Initialize():
        err = CheckConfigVersion()
        if err != None:
            return err
        return None

    def Start(self):
        err = SetMongoDB()

class Commands:
    def __init__(self, config, nrf):
        self.config = config
        self.nrf = nrf

a = NrfConfig.Info
