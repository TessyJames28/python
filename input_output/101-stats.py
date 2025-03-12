#!/usr/bin/python3
import sys

""" Write a script that reads stdin line by line and computes metrics:
"""

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

file_size = 0
counter = 0
try:
    for line in sys.stdin:
        line = line.strip()
        values = line.split()
        status = values[-2]
        size = values[-1]
        
        if status in status_codes:
            status_codes[status] += 1
        file_size += int(size)
        counter += 1

        if counter % 10 == 0:
            print(f"file size: {file_size}")
            for key, val in status_codes.items():
                print(f"{key}: {val}")
except KeyboardInterrupt as e:
    print(f"file size: {file_size}")
    for key, val in status_codes.items():
        print(f"{key}: {val}")
    raise e