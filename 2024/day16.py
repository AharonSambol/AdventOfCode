import bisect

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve(board: list[str], dir_pos: int) -> tuple[int, int]:
    pos = next((r, c) for r, row in enumerate(board) for c, x in enumerate(row) if x == 'S')
    queue = [(board, pos, dir_pos, set(), 0)]
    visited = {}
    min_cost = None
    positions_to_sit = {pos}
    while True:
        board, pos, dir_pos, positions_on_path, cost = queue.pop(0)
        if min_cost and cost > min_cost:
            break
        if board[pos[0]][pos[1]] == 'E':
            min_cost = cost
            positions_to_sit.update(positions_on_path)
            continue
        for dir_change, step_cost in ((0, 1), (1, 1001), (-1, 1001)):
            new_dir_pos = (dir_pos + dir_change) % len(DIRECTIONS)
            new_pos = pos[0] + DIRECTIONS[new_dir_pos][0], pos[1] + DIRECTIONS[new_dir_pos][1]
            if board[new_pos[0]][new_pos[1]] != '#':
                new_cost = cost + step_cost
                if new_cost > visited.get((new_pos, new_dir_pos), new_cost):
                    continue
                visited[(new_pos, new_dir_pos)] = new_cost
                bisect.insort(
                    queue,
                    (board, new_pos, new_dir_pos, positions_on_path | {new_pos}, new_cost),
                    key=lambda x: x[-1]
                )
    return min_cost, len(positions_to_sit)


def main():
    with open('inputs/day16.txt') as f:
        board = f.read().split('\n')
    print(solve(board, 0))


if __name__ == '__main__':
    main()
