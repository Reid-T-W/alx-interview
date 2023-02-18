#!/usr/bin/python3
""" Analyze Logs and print summary of file sizes and status codes"""
import sys
import re


status_code_dict = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

total_size = 0
counter = 0

try:
    for line in sys.stdin:
        # print(line)
        tokens = line.split()
        if len(tokens) < 2:
            continue
        file_size = int(tokens[-1])
        status = int(tokens[-2])
        counter = counter + 1
        total_size = total_size + file_size
        status_code_dict[status] = status_code_dict[status] + 1

        if (counter == 10):
            print("File size: {}".format(total_size))
            status_code_dict_sorted = sorted(status_code_dict.items())
            for code, count in dict(status_code_dict_sorted).items():
                if count != 0:
                    print("{}: {}".format(code, count))
            counter = 0
finally:
    # This is required in cases were the total number of logs is not
    # divisible by 10
    # Example if their are 19 logs, the first ten will be handled with
    # the above code, but the loop will exit without processing the
    # remaining 9, the code below prints out the summary of the 9 logs.
    if counter != 0:
        print("File size: {}".format(total_size))
        status_code_dict_sorted = sorted(status_code_dict.items())
        for code, count in dict(status_code_dict_sorted).items():
            if count != 0:
                print("{}: {}".format(code, count))
