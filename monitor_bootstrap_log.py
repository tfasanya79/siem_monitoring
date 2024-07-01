#!/usr/bin/env python3

import time

def monitor_bootstrap_log():
    log_file = "/var/log/bootstrap.log"
    keywords = ["error", "fail", "panic"]

    while True:
        with open(log_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if any(keyword in line.lower() for keyword in keywords):
                    print(f"Keyword found in {log_file}: {line.strip()}")
        time.sleep(10)

if __name__ == "__main__":
    monitor_bootstrap_log()
