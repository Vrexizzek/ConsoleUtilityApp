from functions.base.utils import log, log_console
import time

def timer():
        times = int(input("Time: "))
        x = 0
        log("Timer, {} sec.".format(times))
        while x < times:
            time.sleep(1)
            log_console("INFO", str(times - x))
            x += 1