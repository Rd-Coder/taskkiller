import _clitools
import psutil, time, os
from _clitools import ANSI, printcl
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

class TaskKiller:

    @classmethod
    def killProcess(
        cls, process: psutil.Process, isApp: bool, retry: bool=False, timeout=5
    ) -> bool:        
        PLAY_ANIMATION = True
        wait_animation = _clitools.animate_wait(lambda: PLAY_ANIMATION)

        try:
            name = process.name()
            identifier = 'processo' if isApp else 'serviço'
            print(f'Terminando {identifier} {name}', end='', flush=True)

            wait_animation.start()

            process.terminate()
            process.wait(timeout)

            PLAY_ANIMATION = False
            wait_animation.join()

            printcl('OK', ANSI.GREEN)
        except:
            PLAY_ANIMATION = False
            wait_animation.join()
            printcl('Erro', ANSI.RED)

            if not retry:
                TaskKiller.killProcess(process, isApp, True, timeout*2)
            return False
        return True

    def killProcesses(self, apps: tuple, services: tuple, ignoreTuple: tuple, verifyAtEnd=True) -> set:
        ignoredSet:set = set()
        
        for proc in psutil.process_iter():
            name = proc.name()
            try:
                isApp = False
                hasSucceed = False

                if name.startswith(ignoreTuple):
                    if not(name in ignoredSet):
                        ignoredSet.add(name)
                        printcl(name+ ' ignorado.', ANSI.GREY, flush=True)
                    continue

                if (name.startswith(apps)):
                    isApp = True
                    hasSucceed = TaskKiller.killProcess(proc, isApp)
                elif name.startswith(services):
                    isApp = False
                    hasSucceed = TaskKiller.killProcess(proc, isApp)
            except:
                raise # TODO make error explicit
        
        if (verifyAtEnd):
            print('\n> Verificando se tá tudo certo...')
            self.killProcesses(apps, services, ignoreTuple, verifyAtEnd=False)

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
