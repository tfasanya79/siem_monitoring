#!/usr/bin/env python3

import subprocess

def check_service_status(service_name):
    try:
        subprocess.run(['systemctl', 'is-active', '--quiet', service_name], check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def restart_service(service_name):
    subprocess.run(['systemctl', 'restart', service_name])

def monitor_services(service_list):
    for service in service_list:
        if not check_service_status(service):
            print(f"Warning: Service {service} is not running. Attempting to restart.")
            restart_service(service)

if __name__ == "__main__":
    services_to_monitor = ['nginx', 'mysql']
    monitor_services(services_to_monitor)
