#!/usr/bin/env python3

import socket

def scan_ports(host='localhost', port_range=(1, 65535)):
    open_ports = []
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

if __name__ == "__main__":
    open_ports = scan_ports()
    if open_ports:
        print(f"Alert: Open ports detected - {open_ports}")
