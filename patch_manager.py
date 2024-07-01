#!/usr/bin/env python3

import subprocess

def check_for_updates():
    result = subprocess.run(['sudo', 'apt', 'update'], capture_output=True, text=True)
    if "packages can be upgraded" in result.stdout:
        print("Alert: System updates are available.")
        subprocess.run(['sudo', 'apt', 'upgrade', '-y'])

if __name__ == "__main__":
    check_for_updates()

