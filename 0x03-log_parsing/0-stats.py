#!/usr/bin/python3
"""
This module contains a script that reads from stdin line by line and computes
metrics.
"""


import sys

possible_status_code = {'200': 0, '301': 0, '400': 0, '401': 0,
                        '403': 0, '404': 0, '405': 0, '500': 0}
total_file_size = 0
count = 0

try:
    for line in sys.stdin:
        split_line = line.split(" ")
        if len(split_line) > 4:
            code = split_line[-2]
            new_size = int(split_line[-1])
            if code in possible_status_code.keys():
                possible_status_code[code] += 1
            total_file_size += new_size
            count += 1

        if count == 10:
            count = 0
            print('File size: {}'.format(total_file_size))
            for key, value in sorted(possible_status_code.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as e:
    pass

finally:
    print('File size: {}'.format(total_file_size))
    for key, value in sorted(possible_status_code.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
