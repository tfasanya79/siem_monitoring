#!/usr/bin/env python3

import os
import hashlib
import time

# Configuration
backup_dir = "/path/to/your/backup"
expected_files = {
    "backup1.tar.gz": "expected_md5_hash1",
    "backup2.tar.gz": "expected_md5_hash2",
    # Add more backups and their expected MD5 hashes here
}
check_interval = 3600  # Check every hour

def calculate_md5(file_path):
    """Calculate the MD5 checksum of a file."""
    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    except FileNotFoundError:
        return None

def verify_backup_files():
    """Verify the integrity of the backup files."""
    missing_files = []
    for file_name, expected_md5 in expected_files.items():
        file_path = os.path.join(backup_dir, file_name)
        if not os.path.exists(file_path):
            missing_files.append(file_name)
        else:
            actual_md5 = calculate_md5(file_path)
            if actual_md5 is None:
                print(f"Alert: Backup file {file_name} is missing.")
            elif actual_md5 != expected_md5:
                print(f"Alert: Backup file {file_name} verification failed. Expected {expected_md5}, got {actual_md5}.")
            else:
                print(f"Backup file {file_name} verified successfully.")

    if missing_files:
        print(f"Alert: Missing backup files: {', '.join(missing_files)}")

if __name__ == "__main__":
    while True:
        verify_backup_files()
        time.sleep(check_interval)

