import socket

def scanner(host, ports):

    try:
        ip = socket.gethostbyname(host) # Resolve hostname to IP address
    except socket.gaierror:
        print("Invalid host or IP address.")

    print(f"Scanning for open ports on {ip}")

    for port in ports:
        try:
            tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP socket
            tcp_sock.settimeout(1) # 1 second timeout
            conn = tcp_sock.connect_ex((ip, port)) # Trying to connect 
            if conn==0: # connect_ex returns 0 if connection is successful.
                print(f"Port {port}: Open")
        except socket.error as e:
            print(f"Error connectiong to port {port}: {e}")
        
if __name__ == '__main__':
    host = input("Enter the IP address or hostname: ")
    ports_str = input("Enter a comma-separated list of ports (e.g. 21,22,23,80): ")
    ports = [int(port) for port in ports_str.split(",")] # Convert string to list of integers
    scanner(host, ports)
