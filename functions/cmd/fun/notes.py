from functions.base.utils import slow_type, log

def note():
        from datetime import datetime
        note = input("Enter your note: ")
        with open("data/notes.txt", "a") as nf:
            nf.write(f"{datetime.now()}: {note}\n")
        slow_type("Note saved.")
        log("Note created")
def readnotes():
        try:
            with open("data/notes.txt", "r") as nf:
                notes = nf.read()
            slow_type("Notes:")
            slow_type(notes)
            log("Notes read")
        except FileNotFoundError:
            slow_type("No notes found.")

def clearnotes():
        with open("data/notes.txt", "w") as nf:
            nf.truncate(0)
        slow_type("All notes cleared.")
        log("Notes cleared")