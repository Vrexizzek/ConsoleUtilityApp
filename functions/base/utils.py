import sys
import time
from datetime import datetime

import config


def slow_type(t, typing_speed=config.typing_speed):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(1 / typing_speed)
    print('')


def log_console(level, message):
    colors = {
        "INFO": "\033[94m",
        "OK": "\033[92m",
        "WARN": "\033[93m",
        "FAIL": "\033[91m",
        "SYS": "\033[90m"
    }
    reset = "\033[0m"
    print(f"{colors.get(level, '')}[{level}]{reset} {message}")


def log(text, file_path='data/logs.txt'):
    with open(file_path, 'a') as file:
        file.write(f"[{datetime.now()}] > {text}\n")
