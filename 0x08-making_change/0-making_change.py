#!/usr/bin/python3
""" Determines the minimum number of coins required to get total """


def check_even_or_odd(num):
    """ Check if a number is odd or even """
    if num % 2 == 0:
        return 'even'
    return 'odd'


def makeChange(coins, total):
    """ Find total number of coins required to get total"""
    if total <= 0:
        return 0
    # Checking if total can be met with the coins we have
    # Check if total is odd or even
    total_even_or_odd = total % 2 == 0
    for coin in coins:
        # If this case is satisfied it means that at least
        # one coin is found that can help us get total
        if (coin % 2 == 0) == total_even_or_odd:
            # logic goes here
            # sort the list
            sorted_coins = sorted(coins)
            # Pointer to biggest number (last element of the list)
            first_big = len(sorted_coins) - 1
            # Pointer to second biggest number (second to the last element
            # on the list)
            second_big = first_big - 1
            if coins[first_big] > total:
                first_big -= 1
                second_big -= 1
            # Checking if only the first biggest element can give us the
            # total
            if total % coins[first_big] == 0:
                return (total // coins[first_big])
            if check_even_or_odd(total) == 'odd':
                # odd + even = odd (since total is odd)
                for _ in range(len(coins)):
                    if check_even_or_odd(coins[first_big]) != \
                      check_even_or_odd(coins[second_big]):
                        # logic here
                        first_multiplier = total // coins[first_big]
                        second_multiplier = (total - coins[first_big]) // \
                            coins[second_big]
                        return (first_multiplier + second_multiplier)
                    second_big -= 1
            elif check_even_or_odd(total) == 'even':
                # even + even = even
                # odd + odd = even
                # odd + even = odd (we don't want this since total is even)
                for _ in range(len(coins)):
                    if check_even_or_odd(coins[first_big]) == \
                      check_even_or_odd(coins[second_big]):
                        # logic here
                        first_multiplier = total // coins[first_big]
                        second_multiplier = (total - coins[first_big]) // \
                            coins[second_big]
                        return (first_multiplier + second_multiplier)
                    second_big -= 1
            return 0
    return -1
