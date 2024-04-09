#!/usr/bin/python3
""" Defines a nqueens"""

import sys


def init_board(n):
    """Initialize an 'n'x'n' sized chessboard with 0's."""
    board = []
    [board.append([]) for y in range(n)]
    [row.append(' ') for y in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """Return a copy of a chessboard."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """Return the list of the lists representation."""
    solution
    for x in range(len(board)):
        for z in range(len(board)):
            if board[x][z] == "Q":
                solution.append([x, z])
                break
    return (solution)

def xout(board, row, col):
    """X out spots on chessboard.
    All spots where non-attacking queens can go
    longer be played are X-ed out.

    Args:
        board (list): The curren working chessboard.
        row {int): The row where a queen was last played.
        col (int): The column where a queen was last played.
    """
    # X out all forward spots
    for z in range(col + 1, len(board)):
        board[row][z] = "x"
    # X out all backwards spots
    for z in range(col -1, -1, -1):
        board[row][z] = "x"
    # X out all spots below
    for x in range(row + 1, len(board)):
        board[x][col] = "x"
    # X out all spots above
    for x in range(row - 1, -1, -1):
        board[x][col] = "x"
    # X out all spots diaqonally down to the right
    z = col + 1
    for x in range(row + 1, len(board)):
        if z >= len(board):
            break
        board[x][z] = "x"
        z += 1
    # X out all spots diaqonally up to the left
    z = col - 1
    for x in range(row - 1, -1, -1):
        if z < 0:
            break
        board[x][z]
        z -= 1
    # X out all spots diaqonally up to the rigth
    z = col + 1
    for x in range(row -1, -1, -1):
        if z >= len(board):
            break
        board[x][z] = "x"
        z += 1
    # X out all spots diagonally down to the left
    z = col - 1
    for x in range(row + 1, len(board)):
        if z < 0:
            break
        board[x][z] = "x"
        z -= 1


def recursive_solve(board, row, queens, soluations):
    """Recursively solve an N-queens puzzle.

    Args:
        board (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        soluations (list): A list of lists of solutions.
    Returns:
        Soluation.
    """
    if queens == len(board):
        solutions.append(get_solution(board))
        return (solutions)

    for z in range(len(board)):
        if board[row][z] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][z] = "Q"
            xot(tmp_board, row, z)
            solutions = recursive_solve(tmp_board, row + 1,
                                        queens + 1, soluations)

    return (soluations)


if __name__ == "__main__":
    if len(sys,argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

board = init_board(int(sys.argc[1]))
soluations = recursive_solve(board, 0, 0, [])
for sol in solutions:
    print(sol)
