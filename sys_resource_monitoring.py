#!/usr/bin/env python3

import psutil

def check_cpu_usage(threshold=75):
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > threshold:
        print(f"Alert: High CPU usage detected - {cpu_usage}%")

def check_memory_usage(threshold=75):
    memory_usage = psutil.virtual_memory().percent
    if memory_usage > threshold:
        print(f"Alert: High memory usage detected - {memory_usage}%")

def check_disk_usage(threshold=75):
    disk_usage = psutil.disk_usage('/').percent
    if disk_usage > threshold:
        print(f"Alert: High disk usage detected - {disk_usage}%")

if __name__ == "__main__":
    check_cpu_usage()
    check_memory_usage()
    check_disk_usage()
