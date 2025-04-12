from functions.base.utils import log_console
import os
import sys
import time
import datetime

def startup_sequence(admin_mode=False):
    os.system("cls")
    log_console("SYS", "Beginning startup sequence...")
    time.sleep(0.3)
    if admin_mode:
        log_console("INFO", "Logged as ADMIN")
        log_console("OK", "Admin permissions granted!")
    time.sleep(0.3)
    log_console("INFO", f"Detected {len(sys.modules)} system modules.")
    time.sleep(0.3)
    log_console("INFO", "Loading core systems...")
    frames = [" #..........", " ##.........", " ###........", " ####.......", " #####......",
              " ######.....", " #######....", " ########...", " #########..",
              " ##########.", " ###########"]
    for frame in frames:
        print(frame, end='\r')
        time.sleep(0.2)
    log_console("OK", "System loaded.")
    log_console("SYS", f"System time: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    log_console("OK", "Welcome!" if not admin_mode else "Welcome, Administrator!")