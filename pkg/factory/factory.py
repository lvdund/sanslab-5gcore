from config import Config

NrfConfig = Config

def CheckConfigVersion():
    currentVersion = NrfConfig.Info.Version
    if currentVersion != config.NrfExpectedConfigVersion:
        return "config version is {0}, but expected is {1}.".format(currentVersion, config.NrfExpectedConfigVersion)
    # logger.CfgLog.Infof("config version [%s]", currentVersion)
    return None

