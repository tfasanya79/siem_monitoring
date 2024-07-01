#!/usr/bin/env python3

import psutil
from datetime import datetime

def monitor_user_activity():
    users = psutil.users()
    for user in users:
        started_time = datetime.fromtimestamp(user.started).strftime('%Y-%m-%d %H:%M:%S')
        print(f"User: {user.name}, Terminal: {user.terminal}, Host: {user.host}, Started: {started_time}")

if __name__ == "__main__":
    monitor_user_activity()
