import os, sys, random, socket
from getpass import getpass
from datetime import datetime

from functions.base.utils import slow_type, log_console, log
from functions.base.user import read_users_from_file, hash_password, create_user, delete_user
from functions.base.startup import startup_sequence
from functions.base.nfc import read_nfc_data, write_nfc_data, clear_nfc_data


from functions.cmd.fun import bomb, echo, spam, timer
from functions.cmd.scan import port_scan
from functions.cmd.utility import admin_login, check_ip, clear, help, link, ping, sysinfo, ver


current_user = None
admin_mode = False

def login():
    global current_user, admin_mode
    os.system("cls")
    login_name = input("Login: ")
    password = getpass("Hasło: ")

    users = read_users_from_file()
    if login_name in users and users[login_name]['password'] == hash_password(password):
        current_user = login_name
        admin_mode = users[login_name]["admin"]
        log_console("OK", f"Zalogowano jako {current_user}")
        log(f"Zalogowano: {current_user}")
        return True
    else:
        log_console("FAIL", "Nieprawidłowe dane logowania.")
        return False

def main():
    global current_user, admin_mode

    if not login():
        return

    startup_sequence(admin_mode)

    while True:
        try:
            cmd = input("> ").lower()

            if cmd == "exit":
                log_console("INFO", "Zamykanie programu.")
                break
            
            elif cmd == "help":
                help.help()

            elif cmd == "clear" or cmd == "cls":
                clear.cls()

            elif cmd == "bomb":
                bomb.bomb()

            elif cmd == "echo":
                echo.echo()

            elif cmd == "spam":
                spam.spam()

            elif cmd == "time":
                log_console("INFO", "Czas systemowy: " + str(datetime.now()))

            elif cmd == "timer":
                timer.timer()
            
            elif cmd == "portscan" or cmd == "port_scan" or cmd == "port-scan":
                port_scan.portscan()

            elif cmd == "ping":
                ping.ping()

            elif cmd == "checkip" or cmd == "check_ip" or cmd == "check-ip":
                check_ip.checkip()

            elif cmd == "sysinfo" or cmd == "systeminfo" or cmd == "system-info":
                sysinfo.sysinfo()

            elif cmd == "ver":
                ver.ver()

            elif cmd == "link":
                link.link()

            elif cmd == "link":
                link.link()
            
            elif cmd == "ping":
                ping.ping()

            elif cmd == "nfc":
                nfc_data = read_nfc_data()
                if nfc_data:
                    log_console("OK", f"Odczytano dane NFC: {nfc_data}")
                    write_nfc_data(nfc_data)
                else:
                    log_console("FAIL", "Nie można odczytać danych NFC.")

            elif cmd == "create-user" and admin_mode:
                name = input("Name: ")
                pss = input("Password: ")
                is_admin = input("Is admin? (y/n): ").strip().lower() == "y"
                create_user(name, pss, is_admin)

            elif cmd == "delete-user" and admin_mode or cmd == "delete_user" and admin_mode or cmd == "deleteuser" and admin_mode:
                name = input("Name: ")
                delete_user(name)

            elif cmd == "users" and admin_mode:
                users_dict = read_users_from_file()
                if users_dict:
                    log_console("INFO", "===== USER LIST =====")
                    for i, user in enumerate(users_dict.keys(), start=1):
                        log_console("OK", f"{i}. {user}")
                    log_console("INFO", "======================")
                    log("User list displayed")
                else:
                    log_console("WARN", "No users found.")
                    log("Attempted to display users, but none found.")

            elif cmd == "clear_nfc":
                clear_nfc_data()


            elif cmd == "clear" or cmd == "cls":
                clear.clear()
            

            elif cmd == "exit":
                log_console("INFO", "Zamykanie programu.")
                break

            elif cmd == "admin-login":
                admin_login.adminlogin()


            else:
                log_console("FAIL", "ERROR 003: INCORRECT COMMAND")

        except KeyboardInterrupt:
            print()
            log_console("INFO", "Zamykanie programu.")
            break


if __name__ == "__main__":
    main()