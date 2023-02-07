#!/usr/bin/python3
""" Minimum Operations Problem """
# import math


def minOperations(n) -> int:
    """
    Minimum number of copy and paste operations
    required to get n numbers of H
    """
    if n <= 0:
        return 0
    # if (n == math.inf || n == -math.inf):
    #    return 0
    if n == 1:
        return 1
    else:
        h_count = 1
        copied_h = 1
        copy_op = 0
        paste_op = 0

        while (h_count < n):
            if (n % h_count == 0):
                copy_op = copy_op + 1
                paste_op = paste_op + 1
                copied = h_count
                h_count = h_count + copied
            else:
                paste_op = paste_op + 1
                h_count = h_count + copied
        return (copy_op + paste_op)
