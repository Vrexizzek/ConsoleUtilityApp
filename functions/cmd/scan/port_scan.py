from functions.base.utils import log_console, log
import socket

def portscan():
    try:
        host = input("Enter host: ").strip().lower()
        if host in ["local", "localhost"]:
            host = "127.0.0.1"

        scan_type = input("Wybierz rodzaj skanowania: \n[1] TCP\n[2] UDP (niedostępne w tej wersji)\n> ").strip()

        ports = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]
        log_console("INFO", f"Scanning {host}...")

        if scan_type == "1":
            for port in ports:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(0.5)
                    try:
                        result = s.connect_ex((host, port))
                        if result == 0:
                            log_console("OK", f"Port {port} is OPEN")
                        else:
                            log_console("WARN", f"Port {port} is CLOSED")
                    except socket.gaierror:
                        log_console("ERROR", "Invalid host")
                        break
                    except Exception as e:
                        log_console("ERROR", f"Error on port {port}: {e}")
        else:
            log_console("WARN", "Wybrany typ skanu nie jest jeszcze zaimplementowany.")

        log(f"Port scan on {host}")
    except KeyboardInterrupt:
        log_console("WARN", "Skanowanie przerwane przez użytkownika.")

