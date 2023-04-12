#!/usr/bin/env python3

import sys
import signal

# Initialize counters
total_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

# Define signal handler to print stats on keyboard interrupt (CTRL + C)
def print_stats(signal, frame):
    print("Total file size: File size: {}".format(total_size))
    for code, count in sorted(status_code_counts.items()):
        if count > 0:
            print("{}: {}".format(code, count))
    sys.exit(0)

signal.signal(signal.SIGINT, print_stats)

# Read input line by line
for i, line in enumerate(sys.stdin):
    try:
        ip, _, _, _, _, _, _, _, _, status_code, size = line.split()
        size = int(size)
        total_size += size
        status_code_counts[int(status_code)] += 1
    except ValueError:
        continue
    if (i+1) % 10 == 0:
        print("Total file size: File size: {}".format(total_size))
        for code, count in sorted(status_code_counts.items()):
            if count > 0:
                print("{}: {}".format(code, count))
