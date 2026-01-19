#!/usr/bin/python3
"""
Automation example: Log analyzer
Demonstrates automating log file analysis with Python.
"""

import re
from collections import Counter
from datetime import datetime

def analyze_log(log_file):
    """
    Analyze a log file and generate statistics.
    
    Args:
        log_file: Path to log file to analyze
    """
    error_count = 0
    warning_count = 0
    info_count = 0
    ip_addresses = []
    timestamps = []
    
    try:
        with open(log_file, 'r') as f:
            for line in f:
                # Count log levels
                if 'ERROR' in line:
                    error_count += 1
                elif 'WARNING' in line:
                    warning_count += 1
                elif 'INFO' in line:
                    info_count += 1
                
                # Extract IP addresses (simplified pattern for common cases)
                # For production use, consider more sophisticated IP validation
                ip_match = re.search(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b', line)
                if ip_match:
                    ip_addresses.append(ip_match.group())
        
        # Generate report
        print("=" * 50)
        print("LOG ANALYSIS REPORT")
        print("=" * 50)
        print(f"Total ERROR messages: {error_count}")
        print(f"Total WARNING messages: {warning_count}")
        print(f"Total INFO messages: {info_count}")
        print(f"\nTotal log entries: {error_count + warning_count + info_count}")
        
        if ip_addresses:
            print("\nTop 5 IP addresses:")
            ip_counter = Counter(ip_addresses)
            for ip, count in ip_counter.most_common(5):
                print(f"  {ip}: {count} occurrences")
        
    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found")
    except Exception as e:
        print(f"Error analyzing log: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: ./log_analyzer.py <log_file>")
        print("Example: ./log_analyzer.py /var/log/application.log")
        sys.exit(1)
    
    analyze_log(sys.argv[1])
