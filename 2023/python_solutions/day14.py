import copy
import itertools
from collections import defaultdict


def move(board):
    columns = defaultdict(int)
    for r, row in enumerate(board):
        for c, item in enumerate(row):
            if item == '#':
                columns[c] = r + 1
            elif item == 'O':
                board[r][c] = '.'
                board[columns[c]][c] = 'O'
                columns[c] += 1
    return board


def count(board): return sum(row.count('O') * (len(board) - r) for r, row in enumerate(board))
def rotate(board): return [list(x) for x in zip(*board[::-1])]


def part2(board):
    mp, rev_mp = {}, {}
    for i in itertools.count():
        for _ in range(4):
            board = rotate(move(board))
        st = '\n'.join(''.join(l) for l in board)
        if st in mp:
            res = (1_000_000_000 - mp[st]) % (i - mp[st])
            return count(rev_mp[mp[st] + res - 1].split('\n'))
        mp[st], rev_mp[i] = i, st


with open('../inputs/day14.txt') as file:
    board = [list(line) for line in file.read().split('\n')]
    print(count(move(copy.copy(board))))
    print(part2(board))
