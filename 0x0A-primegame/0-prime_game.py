#!/usr/bin/python3
"""Determine the winner of a prime number game."""


def prime_nums(n):
    """
    The name of the player who won or none for no clear winner.
    """
    prime_numbers = []
    filtered = [True] * (n + 1)
    for prime in range(2, n + 1):
        if (filtered[prime]):
            prime_numbers.append(prime)
            for i in range(prime, n + 1, prime):
                filtered[i] = False
    return prime_numbers


def isWinner(x, nums):
    """
    returns the winner of the game
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for i in range(x):
        prime_numbers = prime_nums(nums[i])
        if len(prime_numbers) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    return 'Maria' if Maria > Ben else 'Ben'
    return None
