#!/usr/bin/python3
""" Prime game with x rounds and n numbers """


def isWinner(x, nums):
    """
    Prime game with x rounds and n numbers
    Args:
        x - number of rounds
        nums - an array of n, n is a set of
               consecutive integers starting
               from 1 up to and incuding n.
    Return:
        Winner of game
    """
    if (x == 0 or len(nums) == 0):
        return None
    # Get max n for nums and populate the is_prime array
    n = max(nums)
    # Iteration stops at n + 1 so that n is included
    is_prime = [True for _ in range(n + 1)]
    # Setting index 0 and 1 to not prime, as it is a known
    # fact
    is_prime[0] = False
    is_prime[1] = False

    # Populating the is_prime array
    # Iteration must stop at n + 1
    # so that n is included
    stop_iteration = n + 1
    for i in range(2, stop_iteration):
        if i * i > n:
            break
        for j in range(2, stop_iteration):
            if (i * j) > n:
                break
            is_prime[i * j] = False

    # Determining the winner in every round
    maria_wins = 0
    ben_wins = 0
    for round in range(x):
        is_prime_count = is_prime[1: nums[round] + 1].count(True)
        if (is_prime_count % 2 == 0 or is_prime_count == 0):
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins == ben_wins:
        return None
    if maria_wins > ben_wins:
        return "Maria"
    return "Ben"
