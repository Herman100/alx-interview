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

# def pascal_triangle(n):
#     """
#     function for pascal's triangle
#     """
#     if n <= 0:
#         return []

#     triangle = [[1]]
#     for i in range(1, n):
#         row = [1]
#         for j in range(1, i):
#             row.append(triangle[i-1][j-1] + triangle[i-1][j])
#         row.append(1)
#         triangle.append(row)

#     return triangle
