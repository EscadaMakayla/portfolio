import socket

print("Welcome to the Port Scanner!")
target = input("Enter the target IP address (e.g., 127.0.0.1 or scanme.nmap.org): ")
print(f"Scanning target: {target}")

start_port = 1
end_port = 1024
print(f"Scanning ports {start_port}-{end_port}...\n")

for port in range(start_port, end_port + 1):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
print("\nPort scanning complete!")
