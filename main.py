import pyfiglet
from ui import *
from commands import *
from colorama import Fore

def main():
    ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
    print(Fore.YELLOW +  ascii_banner)
    print(Fore.BLUE + desc)
    print(Fore.LIGHTGREEN_EX +  menu)
    choose = int(input(Fore.YELLOW + ">> "))

    if choose == 1:

        target = ipOrDomain()

        port_range = input(Fore.LIGHTBLUE_EX + "Insert Max PORT RANGE: from 1-??? (max. 65535)\n")
        # SCANNER
        portScanner(target, port_range)
    elif choose == 2:
        print("NETWORK SCAN")
    else:
        print(Fore.RED + "Don't Waste my time...")
        return 0



if __name__ == '__main__':
    main()