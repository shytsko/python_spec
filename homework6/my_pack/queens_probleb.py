import random
from random import sample

__all__ = ["check_queens_solution", "view_queens_solution", "get_random_queens_set"]

_N = 8
_EMPTY = 0
_QUEEN = 1
_ATTACK = -1


def check_queens_solution(coordinates: set[tuple[int, int]]) -> bool:
    board = [[0 for _ in range(_N)] for _ in range(_N)]
    for row, col in coordinates:
        if board[row][col] != _EMPTY:
            return False
        for i in range(8):
            board[row][i] = _ATTACK
            board[i][col] = _ATTACK
            x = col - row + i
            if 0 <= x < _N:
                board[i][x] = _ATTACK
            x = col + row - i
            if 0 <= x < _N:
                board[i][x] = _ATTACK
        board[row][col] = _QUEEN
    return True


def view_queens_solution(coordinates: set[tuple[int, int]]) -> None:
    board = [["▢" for _ in range(_N)] for _ in range(_N)]
    for row, col in coordinates:
        board[row][col] = '♕'

    print('\n'.join((''.join(row) for row in board)))


def get_random_queens_set() -> set[tuple[int, int]]:
    foo = [x for x in range(_N)]
    rows = random.sample(foo, len(foo))
    columns = random.sample(foo, len(foo))
    return set(zip(rows, columns))
