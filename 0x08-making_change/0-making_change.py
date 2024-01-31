#!/usr/bin/python3
"""
function that determines the fewest number of coins to an amount
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    return the fewest number of coins needed to meet total.
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
