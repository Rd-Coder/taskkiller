from typing import Callable
from enum import Enum
from threading import Thread
import time

class ANSI(Enum):
    RED         = "\033[1;31m"
    GREEN       = "\033[0;32m"
    YELLOW      = "\033[0;33m"
    GREY        = "\033[0;90m"

    RESET       = "\033[0;0m"
    DEL_LINE    = "\x1b[1A\x1b[2K"
    MOVE_LEFT   = "\u001b[nD" # replace n by number of chars to move
    DEL_RIGHT   = "\u001b[0K"


def delete_line():
    print(ANSI.DEL_LINE.value, end="")
    
def delete_chars(qty: int) -> None:
    MOVE_LEFT = ANSI.MOVE_LEFT.value.replace("n", f"{qty+1}")
    DEL_RIGHT = ANSI.DEL_RIGHT.value
    print(MOVE_LEFT, DEL_RIGHT, end='')

def printcl(obj, color: ANSI, sep='', end='\n', flush=False) -> None:
    print(color.value, obj, ANSI.RESET.value, sep=sep, end=end, flush=flush)

def animate_wait(continue_condition: Callable[[], bool]) -> Thread:

    def animation():
        print(' ',end='')
        FRAMES = [' ','.', '..', '...']
        while continue_condition():
            for frame in FRAMES:
                printcl(frame, ANSI.YELLOW, end='', flush=True)
                delete_chars(len(frame))
                time.sleep(0.2)

    return Thread(target=animation)