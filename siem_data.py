#!/usr/bin/env python3

import os
import socket
import platform
import psutil
import json
import requests
from datetime import datetime, timezone

def get_system_info():
    """Gather basic system information."""
    info = {
        "hostname": socket.gethostname(),
        "fqdn": socket.getfqdn(),
        "os": platform.system(),
        "os_version": platform.version(),
        "os_release": platform.release(),
        "architecture": platform.machine(),
        "platform": platform.platform(),
        "processor": platform.processor(),
        "boot_time": datetime.fromtimestamp(psutil.boot_time(), tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z")
    }
    return info

def get_network_info():
    """Gather network information."""
    interfaces = psutil.net_if_addrs()
    stats = psutil.net_if_stats()
    connections = psutil.net_connections(kind='inet')

    network_info = {
        "interfaces": {iface: [addr.address for addr in addrs if addr.family == socket.AF_INET] for iface, addrs in interfaces.items()},
        "interface_stats": {iface: {"isup": stat.isup, "speed": stat.speed} for iface, stat in stats.items()},
        "connections": [{"fd": conn.fd, "family": conn.family, "type": conn.type, "local_address": conn.laddr, "remote_address": conn.raddr, "status": conn.status} for conn in connections]
    }
    return network_info

def get_disk_info():
    """Gather disk usage information."""
    partitions = psutil.disk_partitions()
    disk_usage = {part.mountpoint: psutil.disk_usage(part.mountpoint)._asdict() for part in partitions}

    disk_info = {
        "partitions": partitions,
        "disk_usage": disk_usage
    }
    return disk_info

def get_memory_info():
    """Gather memory usage information."""
    virtual_memory = psutil.virtual_memory()._asdict()
    try:
        swap_memory = psutil.swap_memory()._asdict()
    except RuntimeError:
        swap_memory = {}

    memory_info = {
        "virtual_memory": virtual_memory,
        "swap_memory": swap_memory
    }
    return memory_info

def get_process_info():
    """Gather information about running processes."""
    processes = []
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username', 'status']):
        try:
            proc_info = proc.info
            proc_info['cpu_percent'] = proc.cpu_percent(interval=0.1)
            proc_info['memory_percent'] = proc.memory_percent()
            processes.append(proc_info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    process_info = {
        "processes": processes
    }
    return process_info

def save_to_file(data, filename="siem_data.json"):
    """Save collected data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def send_to_siem_endpoint(data, url):
    """Send collected data to a SIEM endpoint."""
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.status_code, response.text

def main():
    """Main function to gather data and save/send it."""
    siem_data = {
        "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S %Z"),
        "system_info": get_system_info(),
        "network_info": get_network_info(),
        "disk_info": get_disk_info(),
        "memory_info": get_memory_info(),
        "process_info": get_process_info()
    }

    # Save data to a file
    save_to_file(siem_data)

    # Optionally, send data to a SIEM endpoint
    # url = "http://your-siem-endpoint/api"
    # status_code, response_text = send_to_siem_endpoint(siem_data, url)
    # print(f"SIEM Response: {status_code} - {response_text}")

if __name__ == "__main__":
    main()
