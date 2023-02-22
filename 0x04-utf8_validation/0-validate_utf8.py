#!/usr/bin/python3
"""
Determines  if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Determines  if a given data set represents a valid UTF-8 encoding
    """
    valid = None
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
        if len(str_binary) != 8:
            remaining_zeros = 8 - len(str_binary)
            str_binary = '0' * remaining_zeros + str_binary
        if str_binary[0:2] == "10":
            valid = False
            return valid
        elif str_binary[0:1] == "0":
            valid = True
        elif str_binary[0:3] == "110":
            valid = True
        elif str_binary[0:4] == "1110":
            valid = True
        elif str_binary[0:5] == "11110":
            valid = True
    return valid
