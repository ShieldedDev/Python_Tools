import ipaddress
from scapy.all import IP, ICMP, sr1
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP", help="Range of IP's 192.168.1.0/24")
args = parser.parse_args()

def discover_hosts(network):
    """Scans a network for active hosts using ICMP Echo Requests."""
    network_obj = ipaddress.ip_network(network)
    active_hosts = []

    for ip_address in network_obj.hosts(): # Iterate through all usable host IPs in the network
        ip_str = str(ip_address)
        icmp_request = IP(dst=ip_str) / ICMP()
        response = sr1(icmp_request, timeout=1, verbose=0)

        if response:
            active_hosts.append(ip_str)
            print(f"Host {ip_str} is up.")
        else:
            print(f"Host {ip_str} is down.")

    return active_hosts

target_network = args.IP
active_hosts = discover_hosts(target_network)

print(f"Active hosts on {target_network}: {active_hosts}")
