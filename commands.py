import socket #lib used for check ip addresses of domains
import sys
from datetime import datetime
from ui import *
from colorama import Fore

#this function find the main ip of a domain
def domainToIp(domain):
    try:#check
        ip_address = socket.gethostbyname(domain) #get host
        return ip_address #return ip
    except socket.gaierror as e:
        print(Fore.RED + f"IP Find Error for {domain}: {e}") #fail


def ipOrDomain():
    print(Fore.LIGHTYELLOW_EX + ipordomain_ui)
    print(Fore.GREEN + ip_or_domain)
    choose = int(input(">> "))
    if choose == 1:
        ip = input(Fore.LIGHTBLUE_EX + "Insert Target IP Address (X.X.X.X): ")
        return ip
    elif choose == 2:
        domain = input(Fore.LIGHTBLUE_EX + "Insert Target Domain (www.example.com): ")
        return domainToIp(domain)
    else:
        return

def portScanner(target,port_range):

    #Banner
    print(Fore.LIGHTYELLOW_EX + "_" * 50)
    print(Fore.LIGHTYELLOW_EX + "Scanning Target: " + Fore.LIGHTMAGENTA_EX+  target)
    print(Fore.LIGHTYELLOW_EX + "Scanning started at: " + Fore.LIGHTMAGENTA_EX + str(datetime.now()))
    print(Fore.LIGHTYELLOW_EX + "_" * 50)

    try:
        openports = []
        for port in range(1,int(port_range)):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)
            print(Fore.YELLOW + f"Scanning Port [{port}]...")
            result = s.connect_ex((target,port))
            if result == 0:
                print(Fore.GREEN + "[*] Port {} is open".format(port))
                openports.append(port)
            s.close()


        print(Fore.MAGENTA + final_results)
        print(Fore.YELLOW + "Target: " + Fore.LIGHTMAGENTA_EX + target)
        print(Fore.LIGHTYELLOW_EX + "_" * 50)
        for openport in openports:
            print(Fore.LIGHTGREEN_EX + f"[*] Port {openport} is open")
        print(Fore.LIGHTYELLOW_EX + "_" * 50)
    except KeyboardInterrupt:
        print(Fore.RED + "\n Exiting :(")
    except socket.error:
        print((Fore.RED + "\n Host not responding :("))
        sys.exit()