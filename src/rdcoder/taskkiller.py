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
def wait_boot_offset(offset_minutes: int = 5):
    import time

    def get_logon_time_sec():
        import getpass
        import win32.win32net as win

        win_username = getpass.getuser()
        user_info = win.NetUserGetInfo(None, win_username, 2)
        return user_info['last_logon']
    
    LOGON_TIME = get_logon_time_sec()
    SEC_PER_MIN = 60
    OFFSET_MIN = offset_minutes
    interval_min = (time.time() - LOGON_TIME) // SEC_PER_MIN

    user_will_wait_input = ''
    OPTIONS = ['S', 'N']
    while (interval_min < OFFSET_MIN) and (user_will_wait_input not in OPTIONS):
        user_will_wait_input = input(
            f'Quer esperar o tempo de logon de {interval_min} min? (S/N)'
        ).upper()
        
        if user_will_wait == 'S':
            break
        elif user_will_wait == 'N':
            return
        else:
            print(f'Opção {user_will_wait} inválida.')

    while (interval_min := (time.time() - LOGON_TIME) // SEC_PER_MIN) < OFFSET_MIN:
        remaining_time_min = OFFSET_MIN - interval_MIN + 1
        print(f'> Aguarde {remaining_time_min} min desde o logon para começar a limpeza...')
        time.sleep(SEC_PER_MIN)
        ANSI.delete_line()
