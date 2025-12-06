from itertools import count, takewhile

print("part1:", (lambda rows: sum(1 for r, row in enumerate(rows) for c, item in enumerate(row) if item == "@" and sum((r + x in range(len(rows)) and c + y in range(len(rows[0])) and rows[r + x][c + y] == "@") for x, y in [(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]) < 4))([list(x) for x in open("inputs/day04.txt").read().split("\n")]))
print("part2:", (lambda rows: sum(takewhile(lambda x: x, (sum(rows[r].__setitem__(c, '.') or 1 for r, row in enumerate(rows) for c, item in enumerate(row) if item == "@" and sum((r + x in range(len(rows)) and c + y in range(len(rows[0])) and rows[r + x][c + y] == "@") for x, y in[(0, 1), (0, -1), (1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1)]) < 4) for _ in count()))))([list(x) for x in open("inputs/day04.txt").read().split("\n")]))


# --- CLEAN SOLUTION ---

from itertools import product

DIRECTIONS = [x for x in product([0, 1, -1], repeat=2) if x != (0, 0)]


def is_roll(board: list[list[str]], row: int, col: int) -> bool:
    return row in range(len(board)) and col in range(len(board[row])) and board[row][col] == "@"


def remove_rolls(rows: list[list[str]], remove: bool) -> int:
    removed_rolls = 0
    for r, row in enumerate(rows):
        for c, item in enumerate(row):
            if is_roll(rows, r, c) and sum(is_roll(rows, r + x, c + y) for x, y in DIRECTIONS) < 4:
                rows[r][c] = '.' if remove else rows[r][c]
                removed_rolls += 1
    return removed_rolls


def main():
    with open("inputs/day04.txt") as f:
        rows = [list(x) for x in f.read().split("\n")]
    print("part1:", remove_rolls(rows, False))
    res = 0
    while removed_rolls := remove_rolls(rows, True):
        res += removed_rolls
    print("part2:", res)


main()
