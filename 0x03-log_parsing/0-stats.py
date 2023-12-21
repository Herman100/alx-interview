#!/usr/bin/python3
"""
This module contains a script that reads from stdin line by line and computes
metrics as specified in the project requirements.
"""

import sys
import signal

status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
total_size = 0
line_count = 0


def print_stats():
    """
    This function prints the statistics computed from the logs.
    It prints the total file size and the count of each status code.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    """
    This function handles the signal interruption (CTRL + C).
    It prints the statistics and exits the program when the signal occurs.
    """
    print_stats()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            size = int(parts[-1])
            code = parts[-2]

            if code in status_codes:
                status_codes[code] += 1

            total_size += size
            line_count += 1

            if line_count % 10 == 0:
                print_stats()

        except (e):
            continue

except KeyboardInterrupt:
    pass

finally:
    print_stats()
