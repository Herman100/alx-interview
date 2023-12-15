#!/usr/bin/python3
"""
 method that calculates the fewest number of operations
 needed to result in exactly n H characters in the file.
"""


def minOperations(n):
    """
    Returns n H characters in the file.
    """
    number_of_operations = 0
    minimum_operation = 2
    while n > 1:
        while n % minimum_operation == 0:
            number_of_operations += minimum_operation
            n /= minimum_operation
        minimum_operation += 1
    return number_of_operations
