from collections import namedtuple, deque
from multiprocessing import Pool


Pos = namedtuple('Pos', 'r c count')
def find_path(board, end, queue, visited):
    while queue:
        pos = queue.popleft()
        for dr in ((0, 1), (0, -1), (1, 0), (-1, 0)):
            try:
                new_pos = (pos.r + dr[0], pos.c + dr[1])
                if new_pos not in visited and board[new_pos[0]][new_pos[1]] - board[pos.r][pos.c] < 2:
                    if new_pos == end:
                        return pos.count + 1
                    queue.append(Pos(new_pos[0], new_pos[1], pos.count + 1))
                    visited.add(new_pos)
            except IndexError: pass
    return float("inf")

with open("../Inputs/InputDay12.txt") as file:
    board = [[ord(x) for x in line.rstrip()] for line in file]
    start = end = None
    starts = []
    for r, row in enumerate(board):
        for c, val in enumerate(row):
            if val == ord('S'):
                board[r][c], start = ord('a'), Pos(r, c, 0)
            elif val == ord('E'):
                board[r][c], end = ord('z'), (r, c)
            elif val == ord('a'):
                starts.append(Pos(r, c, 0))
    print(find_path(board, end, deque([start]), {(start.r, start.c)}))

    with Pool() as pool:
        results = [pool.apply_async(find_path, (board, end, deque([s]), {(s.r, s.c)})) for s in starts]
        print(min(p.get() for p in results))
    print(int("dsg"))