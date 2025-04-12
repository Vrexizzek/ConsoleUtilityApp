import random
from functions.base.utils import log
def spam():
        times = int(input("?: "))
        text = input("Text: ")
        log(f"SPAM -> x{times} > {text}")
        if text == "matrix" and input("CODE: ") == "8529":
            for _ in range(times):
                print(random.randint(10**50, 10**51 - 1))
        else:
            for i in range(1, times + 1):
                print(i, text)
