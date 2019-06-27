
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

# Attack types enum


class Attacks:
    USERLESS = 0
    USER = 1


# List of supported routers, and their attack type
routers = [
    ("DGL-5500", Attacks.USERLESS),
    ("DIR-855L", Attacks.USERLESS),
    ("DIR-835", Attacks.USERLESS),
    ("DHP-1565", Attacks.USER),
    ("DIR-652", Attacks.USER),
]

## FUNCTIONS ##


def getRouterIP() -> str:
    """ Gets the IP address of the router """

    # Temp return value
    return "192.168.1.1"


def getRouterType(ip: str) -> str:
    """ Parse router configuration page to check router type """

    # Temp return value
    return "DGL-5500"


def isSupported(router_str: str) -> bool:
    """ Check if a router string is supported by this attack """

    # Return if router string is in the first element of each tuple of routers
    return router_str in [router[0] for router in routers]


def getPassword(ip: str, attack_type: int) -> str:
    """ Parses the router configuration for admin password """

    return ""


# Main function
def main():
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


# Do the python thingy
if __name__ == "__main__":
    main()
