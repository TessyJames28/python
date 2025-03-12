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
        values = line.split()
        if values[-2] in status_codes:
            status_codes[values[-2]] += 1
        file_size += values[-1]
        counter += 1
except KeyboardInterrupt as e:
    print(f"file size: {file_size}")
    for key, val in status_codes.items():
        print(f"{key}: {val}")
    raise e

if counter % 10 == 0:
    print(f"file size: {file_size}")
    for key, val in status_codes.items():
        print(f"{key}: {val}")