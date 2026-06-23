import socket
services = {22: "SSH", 80: "HTTP", 443: "HTTPS"}
target = input("Enter Target IP: ")
start_port = int(input("Enter Start Port: "))
end_port = int(input("Enter End Port: "))
open_ports = []
print("\nScanning...\n")
for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((target, port))
    if result == 0:
        open_ports.append(port)
        service = services.get(port, "unknown")
        print(f"Port {port} Open - {service}")
    sock.close()
print("\nScan Complete")
print("Total Open Ports:", len(open_ports))
print("\nOpen Ports:")
for port in open_ports:
    print(port)