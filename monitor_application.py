#!/usr/bin/env python3

import psutil

def monitor_application(app_name):
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        if proc.info['name'] == app_name:
            print(f"Application: {app_name}, PID: {proc.info['pid']}, CPU: {proc.info['cpu_percent']}%, Memory: {proc.info['memory_percent']}%")

if __name__ == "__main__":
    monitor_application('Terminal')
