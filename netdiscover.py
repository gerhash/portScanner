import nmap
from colorama import Fore

class Network(object):
    def __init__(self):
        self.ip = None  # Default IP not provided initially

    def networkscanner(self):
        print(Fore.GREEN + "Scanning network...")

        # Attempt ARP scan to discover potential default gateway (if allowed)
        try:
            nm = nmap.PortScanner()
            nm.scan(hosts='<broadcast>', arguments='-sn --arp')
            potential_gateway = next((host for host in nm.all_hosts() if nm[host]['mac'] == '00:00:5E:00:00:01'), None)
            if potential_gateway:
                print(Fore.GREEN + f"Potential default gateway found at: {potential_gateway}")
                self.ip = potential_gateway
        except Exception as e:  # Catch all exceptions
            print(Fore.YELLOW + "Error occurred during ARP scan. Check logs for details.")

        # If ARP scan fails, use a generic IP range for basic scan
        if not self.ip:
            network = "192.168.1.0/24"
            print(Fore.GREEN + f"Using default network range: {network}")
        else:
            network = self.ip + '/24'

        try:
            nm = nmap.PortScanner()
            nm.scan(hosts=network, arguments='-sn')
            hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
            print(Fore.LIGHTWHITE_EX + "_" * 30)
            for i, (host, status) in enumerate(hosts_list, start=1):  # Add counter 'i'
                print(Fore.LIGHTWHITE_EX + f"{i}. " + Fore.BLUE + "HOST " + Fore.LIGHTMAGENTA_EX + f"{host} " + Fore.BLUE + f"Status: [{status}]")
            print(Fore.LIGHTWHITE_EX + "_" * 30)
            return hosts_list
        except Exception as e:  # Catch all exceptions
            print(Fore.LIGHTRED_EX + "Error occurred during network scan. Check logs for details.")