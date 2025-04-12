from functions.base.utils import log

def help():
        help_text = """
======================= HELP MENU =======================

[GENERAL COMMANDS]
- help           : Show this help menu
- ver            : Display version info
- devlog         : Show recent changes
- echo           : Echo back text
- clear / cls    : Clear the console
- exit           : Exit the program
- time           : Show current time
- sysinfo        : Display system info
- check-ip       : Check IP address of a website
- random         : Generate a random number

[TOOLS]
- link           : Open quick-access links
- timer          : Countdown timer
- bomb           : Simulated bomb timer
- spam           : Spam text or matrix
- ping           : Pong response
- port-scan      : Scan common open ports on a host

[USER MANAGEMENT]
- create-user    : Create a new user (admin only)
- delete-user    : Delete a user (admin only)
- users          : Show user list (admin only)
- admin-login    : Elevate to admin mode

[NFC SYSTEM]
- nfc            : Read / write / clear NFC data

[NOTES SYSTEM]
- note           : Save a note
- read-notes     : Read all notes
- clear-notes    : Clear all notes

=========================================================
"""
        print(help_text)
        log("Help")