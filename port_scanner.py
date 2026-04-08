# Network Port Scanner
# Author: Your Name

import socket
import threading
from datetime import datetime

# Function to scan a single port
def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target_ip, port))

        if result == 0:
            print(f"[OPEN] Port {port}")
        else:
            print(f"[CLOSED] Port {port}")

        s.close()

    except Exception as e:
        print(f"Error scanning port {port}: {e}")


# Main program
def main():
    print("=" * 50)
    print("        NETWORK PORT SCANNER")
    print("=" * 50)

    target = input("Enter target (IP or domain): ")

    try:
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("Invalid target. Please try again.")
        return

    print(f"\nTarget IP: {target_ip}")

    try:
        start_port = int(input("Enter start port: "))
        end_port = int(input("Enter end port: "))
    except ValueError:
        print("Please enter valid port numbers.")
        return

    print("\nScanning started...")
    print("-" * 50)

    start_time = datetime.now()

    threads = []

    # Create threads for faster scanning
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target_ip, port))
        threads.append(t)
        t.start()

    # Wait for all threads to finish
    for t in threads:
        t.join()

    end_time = datetime.now()
    duration = end_time - start_time

    print("-" * 50)
    print("Scanning completed!")
    print(f"Time taken: {duration}")


# Run the program
if __name__ == "__main__":
    main()