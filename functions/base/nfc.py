from functions.base.utils import log, log_console
import serial
import time


def read_nfc_data():
    try:
        ser = serial.Serial('COM6', 9600, timeout=1)
        ser.flush()
        log_console("SYS", "Waiting for NFC card...")
        while True:
            if ser.in_waiting > 0:
                nfc_data = ser.readline().decode('utf-8').strip()
                if nfc_data:
                    return nfc_data
    except serial.SerialException as e:
        log_console("FAIL", f"ERROR: {e}")
        return None

def write_nfc_data(nfc_id):
    with open("data/nfc_data.txt", "a") as file:
        file.write(f"{nfc_id}: {time.ctime()}\n")
    log_console("OK", f"Data written for NFC card: {nfc_id}")
    log(f"Written NFC Data: {nfc_id}")

def clear_nfc_data():
    with open("data/nfc_data.txt", "w") as file:
        file.truncate(0)
    log_console("OK", "NFC data cleared.")
    log("NFC Data cleared.")
