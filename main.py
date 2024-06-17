import pyfiglet
from ui import *
from commands import *
from colorama import Fore
from netdiscover import Network
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
        print(Fore.LIGHTYELLOW_EX + networkscan)
        D = Network()
        hosts = D.networkscanner()
        try:
            choose_host = int(input(Fore.BLUE + "Select Host: "))
            target = hosts[choose_host - 1][0]
        except IndexError:
            print(Fore.LIGHTRED_EX + "Out Of Range!")
            return 0
        print(Fore.LIGHTMAGENTA_EX + f"{target}" + Fore.BLUE + " Selected!")
        port_range = input(Fore.LIGHTBLUE_EX + "Insert Max PORT RANGE: from 1-??? (max. 65535)\n")
        portScanner(target, port_range)
    else:
        print(Fore.RED + "Don't Waste my time...")
        return 0



if __name__ == '__main__':
    main()