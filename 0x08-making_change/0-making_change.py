#!/usr/bin/python3
""" Determines the minimum number of coins required to get total """


# def check_even_or_odd(num):
#     """ Check if a number is odd or even """
#     if num % 2 == 0:
#         return 'even'
#     return 'odd'


# def makeChange(coins, total):
#     """ Find total number of coins required to get total"""
#     if total <= 0:
#         return 0
#     # Checking if total can be met with the coins we have
#     # Check if total is odd or even
#     total_even_or_odd = total % 2 == 0
#     for coin in coins:
#         # If this case is satisfied it means that at least
#         # one coin is found that can help us get total
#         # sort the list
#         coins = sorted(coins)
#         # Pointer to biggest number (last element of the list)
#         first_big = len(coins) - 1
#         # Pointer to second biggest number (second to the last element
#         # on the list)
#         second_big = first_big - 1
#         if coins[first_big] > total:
#             first_big -= 1
#             second_big -= 1
#         # Checking if only the first biggest element can give us the
#         # total
#         if total % coins[first_big] == 0:
#             return (total // coins[first_big])
#         if check_even_or_odd(total) == 'odd':
#             # odd + even = odd (since total is odd)
#             for _ in range(len(coins)):
#                 if (check_even_or_odd(coins[first_big]) !=
#                    check_even_or_odd(coins[second_big])) \
#                    or coins[second_big] == 1 or coins[second_big] == 1:
#                     # logic here
#                     first_multiplier = total // coins[first_big]
#                     second_multiplier = (total - coins[first_big]) // \
#                         coins[second_big]
#                     return (first_multiplier + second_multiplier)
#                 second_big -= 1
#         elif check_even_or_odd(total) == 'even':
#             # even + even = even
#             # odd + odd = even
#             # odd + even = odd (we don't want this since total is even)
#             for _ in range(len(coins)):
#                 if check_even_or_odd(coins[first_big]) == \
#                    check_even_or_odd(coins[second_big]) \
#                    or coins[second_big] == 1 or coins[second_big] == 1:
#                     # logic here
#                     first_multiplier = total // coins[first_big]
#                     second_multiplier = (total - coins[first_big]) // \
#                         coins[second_big]
#                     return (first_multiplier + second_multiplier)
#                 second_big -= 1
#     return -1


# To Do
# Add a check for impossible total because its minimum
# Correct your logic so that
# print(makeChange([1, 2, 5, 10, 25, 50, 100], 972)) returns a 3


def makeChange(coins, total):
    """ Find total number of coins required to get total"""
    num_of_coins = 0
    if total <= 0:
        return 0
    coins = sorted(coins)
    first_big = len(coins) - 1
    # Checking if the mimimum coin we have is
    # greater than total (coins is sorted)
    # In that case total cannot be achieved
    if (coins[0] > total):
        return -1
    # remainder = total % coins[first_big]
    # remaining = total // coins[first_big]
    # if remaining == 0:
    #     num_of_coins = remainder
    #     return num_of_coins
    adj_total = total
    while ((adj_total) != 0 and first_big >= 0):
        if coins[first_big] > adj_total:
            first_big -= 1
        else:
            num_of_coins += (adj_total // coins[first_big])
            adj_total = adj_total % coins[first_big]
            first_big -= 1
    if (adj_total == 0):
        return num_of_coins
    return -1
