import os
from functions.base.utils import log_console

def clear():
        os.system("cls")
        log_console("OK", "Console cleared.")