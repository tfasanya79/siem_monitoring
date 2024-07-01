#!/usr/bin/env python3
import os
import hashlib

def get_file_hash(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def monitor_files(file_list):
    file_hashes = {}
    for file_path in file_list:
        if os.path.exists(file_path):
            file_hashes[file_path] = get_file_hash(file_path)
        else:
            file_hashes[file_path] = None
    return file_hashes

def check_file_integrity(file_list, original_hashes):
    current_hashes = monitor_files(file_list)
    for file_path, original_hash in original_hashes.items():
        if current_hashes[file_path] != original_hash:
            print(f"Warning: Integrity issue detected in {file_path}")

if __name__ == "__main__":
    files_to_monitor = ['/etc/passwd', '/etc/hosts']
    original_hashes = monitor_files(files_to_monitor)
    # Save original_hashes to a file or database for later comparison
    check_file_integrity(files_to_monitor, original_hashes)
