import sys
import hashlib
from datetime import datetime

from functions.base.utils import log_console, log


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def read_users_from_file(file_path='data/users.txt'):
    users = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 3:
                    login, password, is_admin = parts
                    users[login] = {"password": password, "admin": is_admin == "1"}
                elif len(parts) == 2:
                    login, password = parts
                    users[login] = {"password": password, "admin": False}
    except FileNotFoundError:
        log_console("FAIL", f"File {file_path} not found.")
        sys.exit()
    return users


def create_user(login, password, is_admin=False, file_path='data/users.txt'):
    users = read_users_from_file(file_path)
    if login in users:
        log_console("FAIL", "User already exists.")
        return
    from functions.base.user import hash_password
    with open(file_path, 'a') as file:
        file.write(f"{login}:{hash_password(password)}:{'1' if is_admin else '0'}\n")
    log_console("OK", f"User '{login}' created ({'Admin' if is_admin else 'User'}).")
    log(f"Created user: {login} ({'Admin' if is_admin else 'User'})")


def delete_user(login, file_path='data/users.txt'):
    users = read_users_from_file(file_path)
    if login in users:
        del users[login]
        with open(file_path, 'w') as file:
            for user_login, user_data in users.items():
                file.write(f"{user_login}:{user_data['password']}:{'1' if user_data['admin'] else '0'}\n")
        log_console("OK", f"User {login} deleted.")
        log(f"Deleted user: {login}")
    else:
        log_console("FAIL", f"User {login} not found.")
