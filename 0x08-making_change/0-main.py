#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

# print(makeChange([1, 2, 25], 37)) => 7
# print(makeChange([1, 2, 5, 10, 25, 50, 100], 972)) => 13
# print(makeChange([10, 25, 50, 100], 972))


# print(makeChange([1256, 54, 48, 16, 102], 1453)) 
# => -1
print(makeChange([1, 4, 5, 10], 1278652)) 
# => 127867

# # Edge Case 1, only one element (pass)
# print(makeChange([1452], 1453))

# # Edge Case 2, empty list
# print(makeChange([], 1453))

# print(makeChange([1, 25], 37))



# print(makeChange([5, 3, 25], 37))