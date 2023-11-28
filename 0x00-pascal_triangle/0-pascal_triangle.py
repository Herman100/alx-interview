#!/usr/bin/python3
'''
function that returns list of Pascal's triangle of n
'''


from math import factorial


def pascal_triangle(n):
    """
    function for pascal's triangle
    """
    if n <= 0:
        return []

    triangle = []
    for n in range(n):
        row = []
        for r in range(n + 1):
            ncr = factorial(n) // (factorial(r) * factorial(n - r))
            row.append(ncr)
        triangle.append(row)
    return triangle
