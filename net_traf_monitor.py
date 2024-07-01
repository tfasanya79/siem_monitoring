#!/usr/bin/env python3

import psutil
import time

def monitor_network_traffic(threshold=1000000):  # Increased threshold to 1 MB
    old_stats = psutil.net_io_counters()
    try:
        while True:
            new_stats = psutil.net_io_counters()
            bytes_sent = new_stats.bytes_sent - old_stats.bytes_sent
            bytes_recv = new_stats.bytes_recv - old_stats.bytes_recv
            
            # Debug: Print received and sent bytes
            print(f"Bytes sent: {bytes_sent}, Bytes received: {bytes_recv}")

            if bytes_sent > threshold:
                print(f"Alert: High network traffic detected - {bytes_sent} bytes sent")
            if bytes_recv > threshold:
                print(f"Alert: High network traffic detected - {bytes_recv} bytes received")
            
            old_stats = new_stats
            time.sleep(1)  # Adjust sleep time as needed
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")
        # Perform any necessary cleanup actions here

if __name__ == "__main__":
    monitor_network_traffic()
