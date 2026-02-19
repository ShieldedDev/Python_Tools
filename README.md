
# Python Tools

### Crafting Custom Network Scanners with Scapy in Python
    1. icmp.py 
    2. ip_scanner.py 

### Clone the Repository:
    git clone https://github.com/ShieldedDev/Python_Tools/


## 1)  icmp.py :

    usage: sudo python3 icmp.py 192.168.1.1

 This script helps us in host discovery, also known as ping scanning, is the process of identifying active hosts on a network. A simple host discovery scanner can be built using Scapy by sending ICMP Echo Request (ping) packets to a range of IP addresses and analyzing the responses.

  -  IP(dst=ip_address) creates an IP packet with the destination IP address set to ip_address.

  -  ICMP() creates an ICMP Echo Request packet.

  -  / combines the IP and ICMP layers to create a complete packet.

  -  sr1() sends the packet and waits for a single response. timeout specifies the maximum time to wait for a response, and verbose=0 suppresses Scapy's output.


## 2) ip_scanner.py :

    usage: sudo python3 ip_scanner.py 192.168.1.0/24

To scan a range of IP addresses, you can iterate through the addresses and send an ICMP Echo Request to each one.

This script iterates through all the usable IP addresses in the specified network using the `ipaddress` module. For each IP address, it sends an ICMP Echo Request and checks for a response.


## 2) port_scanner.py :

    usage: sudo python3 port_scanner.py 

To scan a range of IP addresses, you can iterate through the addresses and send an ICMP Echo Request to each one.

This script takes a target IP address and a list of ports as input and checks if each port is open.
