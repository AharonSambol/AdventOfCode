from bisect import insort


def part1(board, force_continue, can_continue):
    posses = [(0, (0, 0), None, 0, [(0, 1), (1, 0)])]
    visited = {}
    while posses:
        path_len, pos, cur_dir, amount_in_dir, possible_dirs = posses.pop(0)
        for _dir in possible_dirs:
            new_pos = (pos[0] + _dir[0], pos[1] + _dir[1])
            if new_pos[0] not in range(len(board)) or new_pos[1] not in range(len(board[0])):
                continue

            new_amount_in_dir = amount_in_dir + 1 if _dir == cur_dir else 1
            new_path_len = path_len + board[new_pos[0]][new_pos[1]]
            if (v := visited.get((new_pos, _dir, new_amount_in_dir))) and new_path_len >= v:
                continue
            visited[(new_pos, _dir, new_amount_in_dir)] = new_path_len

            if new_pos == (len(board) - 1, len(board[0]) - 1):
                if new_amount_in_dir >= force_continue:
                    return new_path_len
                continue

            next_dirs = [_dir] if new_amount_in_dir < force_continue else [d for d in [(0, 1), (1, 0), (-1, 0), (0, -1)] if d != (_dir[0] * -1, _dir[1] * -1)]
            if new_amount_in_dir >= can_continue:
                next_dirs.remove(_dir)
            insort(posses, (new_path_len, new_pos, _dir, new_amount_in_dir, next_dirs))


with open('../inputs/day17.txt') as file:
    board = [[int(x) for x in line] for line in file.read().split('\n')]
    print(part1(board, 0, 3))
    print(part1(board, 4, 10))
