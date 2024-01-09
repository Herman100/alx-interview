#!/usr/bin/python3
"""dsa for the famous n queens problem on nxn chessboard"""
import sys


def print_solution(board):
    """print the solution"""
    solution = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                solution.append([i + 1, j + 1])
    print(solution)


def is_safe(board, row, col):
    """check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, len(board), 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_nqueens(board, col):
    """solve the n queens problem using Backtracking"""
    if col == len(board):
        print_solution(board)
        return True
    res = False
    for i in range(len(board)):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0  # backtrack
    return res


def nqueens(n):
    """solve the n queens problem"""
    board = [[0 for _ in range(n)] for _ in range(n)]
    if not solve_nqueens(board, 0):
        print("Solution does not exist")
        return
    return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens(n)