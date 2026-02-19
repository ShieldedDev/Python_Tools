import socket 

def grabber(host, port):
    try:
        tcp_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_sock.settimeout(5) # Time out to grab the banner
        tcp_sock.connect((host, port))

        req = b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n"
        tcp_sock.send(req) # Send a simple HTTP request

        banner = tcp_sock.recv(1024) # Receive up 1024 bytes
        print(banner.decode(errors="ignore"))
        tcp_sock.close()

    except socket.error as e:
        print(f"Error connecting to {host}:{port}: {e}")
    except UnicodeDecodeError:
        print(f"Could not decode banner for {ip}:{port}")

if __name__ == "__main__":
    ip = input("Enter target IP address: ")
    port = int(input("Enter the port number: "))
    grabber(ip, port)
