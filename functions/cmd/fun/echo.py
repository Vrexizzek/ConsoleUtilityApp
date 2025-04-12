from functions.base.utils import slow_type, log

def echo():
        echo = input()
        slow_type(echo)
        log(f"Echo - {echo}")