import socket
from functions.base.utils import slow_type, log_console, log

def checkip():
        web = input("Website adress (etc. www.youtube.com): ")
        ip = socket.gethostbyname(web)
        slow_type(f"\n{ip}\n")
        log(f"CheckIP: web: {web} / IP: {ip}")