import factory

NrfDefaultCertPemPath        = "./config/cert/nrf.pem"
NrfDefaultPrivateKeyPath     = "./config/cert/nrf.key"
NrfDefaultRootCertPemPath    = "./config/cert/root.pem"
NrfDefaultRootPrivateKeyPath = "./config/cert/root.key"
NrfExpectedConfigVersion     = "1.0.2"
NrfSbiDefaultIPv4            = "127.0.0.10"
NrfSbiDefaultPort            = 8000
NrfSbiDefaultScheme          = "https"
NrfNfmResUriPrefix           = "/nnrf-nfm/v1"
NrfDiscResUriPrefix          = "/nnrf-disc/v1"

class Info:
    def __init__(self, Version, Description):
        self.Version = Version
        self.Description = Description

class Cert:
    def __init__(self, Pem, Key):
        self.Pem = Pem
        self.Key = Key

class Sbi:
    def __init__(self, Scheme, RegisterIPv4, BindingIPv4, Port, Cert, RootCert, OAuth):
        self.Scheme = Scheme
        self.RegisterIPv4 = RegisterIPv4
        self.BindingIPv4 = BindingIPv4
        self.Port = Port
        self.Cert = Cert
        self.RootCert = RootCert
        self.OAuth = OAuth

class Configuration:
    def __init__(self, Sbi = Sbi(), MongoDBName = '', MongoDBUrl = '', DefaultPlmnId = 0, ServiceNameList = list()):
        self.Sbi = Sbi
        self.MongoDBName = MongoDBName
        self.MongoDBUrl = MongoDBUrl
        self.DefaultPlmnId = DefaultPlmnId
        self.ServiceNameList = ServiceNameList

class Config:
    def __init__(self, Info = Info(), Configuration = Configuration(), Logger = ''):
        self.Info = Info
        self.Configuration = Configuration
        self.Logger = Logger
        
    