
<img src="" alt="PortScanner" width="700" height="500">

# PortScanner
<img src="https://skillicons.dev/icons?i=py" alt="Skills" />
## Overview
This script allows you to scan the ports of an IP / Domain and do an ARP scan in your network to check the connected devices and then do a port scan of the selected device

## Purpose
The purpose of this script is to perform a multi-step reconnaissance operation on a network:

Port Scanning: It scans the ports of a specified IP address or domain to identify open ports. This can reveal what services are running on the target machine and potential vulnerabilities.
ARP Scanning: It performs an ARP scan on your network to discover connected devices. ARP (Address Resolution Protocol) helps map IP addresses to MAC addresses (physical addresses) on a network. This can be used to identify the number and type of devices on your network.
Focused Port Scanning: Based on the ARP scan results, you can select a specific device identified by its IP address. The script then performs another port scan on this chosen device for a more detailed analysis of its exposed services and potential vulnerabilities.
In summary, this script automates the process of gathering information about a network and its connected devices, potentially for security assessment purposes.


## Usage
1. Install the required dependencies listed in `requirements.txt`.
   
 ```sh
   pip install -r requirements.txt
 ```

2. Run the main.py script to start the Tool
   
 ```sh
  python main.py
 ```





