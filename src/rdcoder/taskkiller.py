from enum import Enum
class ProcessesEnum(Enum):
    APPS: list = [
        'msedge', 'chrome', 'yourphone', 'PhoneExperienceHost.exe', 'OfficeClickToRun.exe', 'OfficeC2RClient.exe',
        'SDXHelper.exe',
        'Dsapi.exe', 'SupportAssistAgent.exe', 'backgroundTaskHost.exe', 'GameBar.exe',
        'CCXProcess.exe', 'AdobeIPCBroker.exe', 'figma_agent.exe', 'DPM.exe', 'msedge*', 'winrar*',
        'Video.UI.exe', 'microsoft.windowscommunicationsapps_16005.14326.21238.0_x64__8wekyb3d8bbwe',
        'PhotosApp.exe', 'PhotosService.exe',
        'MicrosoftEdgeUpdate.exe', 'GoogleUpdate.exe'
    ]

    SERVICES: list = [
        'TapiSrv', 'InstallService', 'DSAService', 'Spooler', 'gamingservicesnet.exe',
        'gameinputsvc.exe', 'gamingservices.exe', 'gamingservices'
    ]
