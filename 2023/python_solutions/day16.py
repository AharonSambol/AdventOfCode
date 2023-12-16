import itertools
from queue import Queue

DIRECTIONS = U, D, R, L = (-1, 0), (1, 0), (0, 1), (0, -1)
MIRRORS = {
    '/': {R: (U,), D: (L,), L: (D,), U: (R,)},
    '\\': {R: (D,), U: (L,), L: (U,), D: (R,)},
    '-': {R: (R,), L: (L,), U: (R, L), D: (R, L)},
    '|': {U: (U,), D: (D,), L: (U, D), R: (U, D)},
}


def move(board, pos, direction, mirror_visited):
    visited = {pos}
    queue = Queue()
    queue.put((pos, direction))
    while not queue.empty():
        pos, direction = queue.get()
        if board[pos[0]][pos[1]] == '.':
            directions = [direction]
        else:
            mirror = MIRRORS[board[pos[0]][pos[1]]]
            directions = mirror[direction]
            if (pos, direction) in mirror_visited:
                continue
            mirror_visited.add((pos, direction))
            for d in (directions if len(directions) == 1 else DIRECTIONS):
                mirror_visited.add((pos, (-d[0], -d[1])))
        for d in directions:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            if new_pos[0] in range(len(board)) and new_pos[1] in range(len(board[0])):
                visited.add(new_pos)
                queue.put((new_pos, d))
    return len(visited)


with open('../inputs/day16.txt') as file:
    board = file.read().split('\n')
    print(move(board, (0, 0), R, set()))

    top = (((0, c), D) for c in range(len(board[0])))
    bottom = (((len(board) - 1, c), U) for c in range(len(board[0])))
    left = (((0, r), R) for r in range(len(board)))
    right = (((r, len(board[0]) - 1), L) for r in range(len(board)))
    print(max(move(board, pos, direction, set()) for pos, direction in itertools.chain(top, bottom, right, left)))
