from functions.base.utils import slow_type, log

def link():
        slow_type("Choose link: \n Youtube -> YT \n Discord -> DC \n Google -> G \n Github -> GH")
        lk = input()
        log("Link.")
        links = {"YT": "https://youtube.com", "DC": "https://discord.com", "G": "https://google.com", "GH": "https://github.com"}
        slow_type(f"{links.get(lk, 'Unknown')}")