import socket
import requests
import os

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
    "DGL-5500": Attacks.USERLESS,
    "DIR-855L": Attacks.USERLESS,
    "DIR-835": Attacks.USERLESS,
    "DHP-1565": Attacks.USER,
    "DIR-652": Attacks.USER
}

# TUI menu
menu = {
    1:{"title": "Display password", "function": lambda: print(router.password)}
}

## FUNCTIONS ##


def getRouterIP() -> str:
    """ Gets the IP address of the router """

    # Temp return value
    return "192.168.1.1"


def getRouterType(ip: str) -> str:
    """ Parse router configuration page to check router type """

    # Temp return value
    return ""


def isSupported(router_str: str) -> bool:
    """ Check if a router string is supported by this attack """

    # Return if router string is in the first element of each tuple of routers
    return router_str in routers


def getPassword(ip: str, attack_type: int) -> str:
    """ Parses the router configuration for admin password """

    return ""


def checkDNS() -> str:
    return socket.gethostbyname("dlinkrouter.local")


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
    print(ASCII.Reset + "   [ ] Search for router via DNS...", end="\r")

    try:
        router.ip = checkDNS()
    except:
        router.ip = ""

    if router.ip != "":
        status_str = ASCII.Green + \
            "   [*] " if router.model != "" else ASCII.Yellow + "   [ ] "
        print(ASCII.Green + "   [*] " + ASCII.Reset +
              "Found router ip via DNS         ")
    else:
        # Check for router IP
        router.ip = getRouterIP()
        print(ASCII.Green + "   [*] " + ASCII.Reset +
              "Found router ip via gateway          ")

    # Check router type
    router.model = getRouterType(router.ip)
    status_str = ASCII.Green + \
        "   [*] " if router.model != "" else ASCII.Yellow + "   [ ] "
    print(status_str + ASCII.Reset + "Check router type")

    # Check if oruter is PWNable
    is_pwnable = isSupported(router.model)
    status_str = ASCII.Green + \
        "   [*] " if is_pwnable else ASCII.Yellow + "   [ ] "
    print(status_str + ASCII.Reset + "Check router support")

    # exit if router is not supported
    if not is_pwnable:
        print("\nRouter is not supported by PWNlink")
        exit(1)

    # Check for password
    router.password = getPassword(router.ip, routers[router.model])

    # Display the menu



# Do the python thingy
if __name__ == "__main__":
    main()
    print(ASCII.Reset)
