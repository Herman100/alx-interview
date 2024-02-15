#!/usr/bin/python3
"""Determine the winner of a prime number game."""


def isWinner(x, nums):
    """
    The name of the player who won or none for no clear winner.
    """
    winners = []
    for n in nums:
        numbers = list(range(1, n+1))
        turn = 'Maria'
        while True:
            primes = [num for num in numbers
                      if all(num % i != 0 for i in
                             range(2, int(num**0.5) + 1))]
            if not primes:
                winners.append('Ben' if turn == 'Maria' else 'Maria')
                break
            prime = min(primes)
            numbers = [num for num in numbers if num % prime != 0]
            turn = 'Ben' if turn == 'Maria' else 'Maria'
    if winners.count('Maria') > winners.count('Ben'):
        return 'Maria'
    elif winners.count('Maria') < winners.count('Ben'):
        return 'Ben'
    else:
        return None
