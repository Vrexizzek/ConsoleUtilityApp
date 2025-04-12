import random
from functions.base.utils import slow_type, log_console, log

def random():
      
        low = int(input("Enter minimum number: "))
        high = int(input("Enter maximum number: "))
        rand_num = random.randint(low, high)
        slow_type(f"Generated number: {rand_num}")
        log(f"Random number generated: {rand_num} ({low}-{high})")