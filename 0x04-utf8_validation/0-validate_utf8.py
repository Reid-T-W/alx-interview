#!/usr/bin/python3
"""
Determines  if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines  if a given data set represents a valid UTF-8 encoding
    """
    valid = True
    for item in data:
        # Extracting the least significant 8 bits
        # The bits are converted to string in order
        # to be able to extract them and perform length
        # checks
        str_binary = str(bin(item))[2:]

        # Checking if the bits start with the number 1
        # in which case it is invalid UTF-8 encoding.
        # Valid encodings start with the 0 bit, only
        # continuation bytes start with the 1 bit.
        # If the first bit of the 8 bits is a zero, python
        # does not display it, hence the length of the bits
        # reduce to 7, but if the leading bit is a one, python
        # displays it, making the length 8.
        if len(str_binary) == 8:
            valid = False
    return valid

# data = [65]
# data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
# data = [229, 65, 127, 256]
# print(validUTF8(data))
