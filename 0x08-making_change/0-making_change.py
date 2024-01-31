# !/usr/bin/python3
"""
This module contains a function that determines
the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Parameters:
    coins (List[int]): A list of the values of the coins in your possession.
    total (int): The total amount to meet.

    Returns:
    int: The fewest number of coins needed to meet total.
    If total is 0 or less,
    return 0. If total cannot be met by any number
    of coins you have, return -1.
    """
    if total <= 0:
        return 0

    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:

        for current_total in range(coin, total + 1):
            min_coins[current_total] = min(min_coins[current_total],
                                           min_coins[current_total - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
