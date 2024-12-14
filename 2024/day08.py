import itertools
import time
from collections import defaultdict


def solve(is_part1: bool, antennas: dict[str, list], board: list[str]) -> int:
    res = set()
    for antenna_typ, antenna_posses in antennas.items():
        for i, antenna_pos in enumerate(antenna_posses):
            for other_antenna_pos in antenna_posses[i + 1:]:
                for a, b in [(antenna_pos, other_antenna_pos), (other_antenna_pos, antenna_pos)]:
                    for repeat in ([1] if is_part1 else itertools.count()):
                        pos = a[0] + repeat * (a[0] - b[0]), a[1] + repeat * (a[1] - b[1])
                        if 0 <= pos[0] < len(board) and 0 <= pos[1] < len(board[0]):
                            res.add(pos)
                        else:
                            break
    return len(res)


def main():
    with open('inputs/day08.txt') as f:
        antennas = defaultdict(list)
        board = f.read().split("\n")
        for r, line in enumerate(board):
            for c, x in enumerate(line):
                if x != ".":
                    antennas[x].append((r, c))
        print(solve(True, antennas, board))
        print(solve(False, antennas, board))


if __name__ == '__main__':
    main()
