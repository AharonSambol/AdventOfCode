import re
from itertools import count


with open("../Inputs/InputDay23.txt") as file:
    board = {}
    for r, line in enumerate(file):
        for c in re.finditer(r'#', line):
            board[pos] = (pos := (r, c.start()))
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for i in count(1):
        new_board = {}
        for elf in board:
            if sum((elf[0] + i, elf[1] + j) in board for i in range(-1, 2) for j in range(-1, 2)) == 1:
                new_board[elf] = elf
                continue
            for dr in dirs:
                new_posses = [(elf[0] + dr[0] + dr[1] * x, elf[1] + dr[1] + dr[0] * x) for x in (0, 1, -1)]
                if any(p in board.keys() for p in new_posses):
                    continue

                if new_posses[0] in new_board:
                    new_board[elf] = elf
                    if new_board[new_posses[0]] is not None:
                        new_board[new_board[new_posses[0]]] = new_board[new_posses[0]]
                        new_board[new_posses[0]] = None
                else:
                    new_board[new_posses[0]] = elf
                break
            else:
                new_board[elf] = elf
        if board == new_board:
            print('part2:', i)
            break
        board = {k: k for k, v in new_board.items() if v}
        dirs.append(dirs.pop(0))
        if i == 10:
            min_r, max_r = min(board, key=(key := lambda x: x[0]))[0], max(board, key=key)[0]
            min_c, max_c = min(board, key=(key := lambda x: x[1]))[1], max(board, key=key)[1]
            print('part1', (max_r - min_r + 1) * (max_c - min_c + 1) - len(board))
