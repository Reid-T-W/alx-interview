#!/usr/bin/python3
""" Analyze Logs and print summary of file sizes and status codes"""
import sys
import re
from collections import defaultdict


# compiling the correct pattern
pat = re.compile(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3} - "
                 r"\[[0-9]{4}-[0-9]{2}-[0-9]{1,2} [0-9]{2}:[0-9]{2}:"
                 r"[0-9]{2}.[0-9]{6}\] "
                 r"\"GET \/projects\/260 HTTP\/1.1\" [0-9]{3} [0-9]*")
total_size = 0
status_code_dict = {}
status_code_dict = defaultdict(lambda: 0, status_code_dict)
counter = 0
for line in sys.stdin:
    # Check input format of line
    if re.match(pat, line):
        # Extract file size
        params = line.split()
        file_size = int(params[-1])
        status = int(params[-2])
        counter = counter + 1
    else:
        counter = counter + 1
        continue

    total_size = total_size + file_size
    status_code_dict[status] = status_code_dict[status] + 1
    if (counter % 10 == 0):
        print("File size: {}".format(total_size))
        status_code_dict_sorted = sorted(status_code_dict.items())
        for code, count in dict(status_code_dict_sorted).items():
            print("{}: {}".format(code, count))

# This is required in cases were the total number of logs is not
# divisible by 10
# Example if their are 19 logs, the first ten will be handled with
# the above code, but the loop will exit without processing the
# remaining 9, the code below prints out the summary of the 9 logs.
if (counter % 10 != 0):
    print("File size: {}".format(total_size))
    status_code_dict_sorted = sorted(status_code_dict.items())
    for code, count in dict(status_code_dict_sorted).items():
        print("{}: {}".format(code, count))
