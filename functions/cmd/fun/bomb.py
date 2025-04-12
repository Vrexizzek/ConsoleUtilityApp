from functions.base.utils import log_console, log
import time

def bomb():
        times = int(input("Time: "))
        x = 0
        log("Bomb, {} sec.".format(times))
        while x < times:
            time.sleep(1)
            log_console("WARN", f"Explosion in {times - x} seconds")
            x += 1
        log_console("FAIL", "BOOM")