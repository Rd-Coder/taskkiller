from typing import Callable

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
    print(color.value, obj, CLColor.RESET.value, sep=sep, end=end, flush=flush)

def animate_wait(cls, continue_condition: Callable[[], bool]) -> Thread:
    from threading import Thread

    def animation():
        print(' ',end='')
        FRAMES = [' ','.', '..', '...']
        while continue_condition():
            for frame in FRAMES:
                printcl(frame, CLColor.YELLOW, end='', flush=True)
                CLColor.delete_chars(len(frame))
                time.sleep(0.2)

    return Thread(target=animation)