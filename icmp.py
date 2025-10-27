from scapy.all import IP, ICMP, sr1
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("host")
args = parser.parse_args()

def discover_host(ip_address):
    """Sends an ICMP Echo Request to the specified IP address and returns True if a response is received."""
    icmp_request = IP(dst=ip_address) / ICMP()  # Construct IP/ICMP packet
    response = sr1(icmp_request, timeout=2, verbose=0)  # Send and receive a single packet

    if response:
        return True
    else:
        return False


if discover_host(args.host):
    print(f"Host {args.host} is up.")
else:
    print(f"Host {args.host} is down.")
