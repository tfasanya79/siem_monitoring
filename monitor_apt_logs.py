#!/usr/bin/env python3

import time

def monitor_apt_logs():
    apt_logs = ["/var/log/apt/history.log", "/var/log/apt/term.log", "/var/log/dpkg.log"]
    keywords = ["install", "upgrade", "remove"]

    while True:
        for log_file in apt_logs:
            with open(log_file, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    if any(keyword in line for keyword in keywords):
                        print(f"Keyword found in {log_file}: {line.strip()}")
        time.sleep(10)

if __name__ == "__main__":
    monitor_apt_logs()
