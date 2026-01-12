#!/usr/bin/python3
"""
Automation example: Batch file renamer
This script demonstrates how ChatGPT can help automate repetitive tasks.
"""

import os
import sys

def rename_files(directory, old_pattern, new_pattern):
    """
    Rename files in a directory by replacing a pattern.
    
    Args:
        directory: Directory containing files to rename
        old_pattern: Pattern to search for in filenames
        new_pattern: Pattern to replace with
    """
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a valid directory")
        return
    
    renamed_count = 0
    for filename in os.listdir(directory):
        if old_pattern in filename:
            old_path = os.path.join(directory, filename)
            new_filename = filename.replace(old_pattern, new_pattern)
            new_path = os.path.join(directory, new_filename)
            
            try:
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")
                renamed_count += 1
            except Exception as e:
                print(f"Error renaming {filename}: {e}")
    
    print(f"\nTotal files renamed: {renamed_count}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./file_renamer.py <directory> <old_pattern> <new_pattern>")
        print("Example: ./file_renamer.py ./docs test_ prod_")
        sys.exit(1)
    
    rename_files(sys.argv[1], sys.argv[2], sys.argv[3])
