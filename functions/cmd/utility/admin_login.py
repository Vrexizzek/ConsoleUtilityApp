from functions.base.utils import log_console, log
import config

def adminlogin():
        if input("ACCESS CODE: ") == config.admin_code:
            admin = True
            log_console("OK", "Admin permissions granted!")
            log("Admin permissions granted.")
        else:
            log_console("FAIL", "ERROR 005: CODE INCORRECT")