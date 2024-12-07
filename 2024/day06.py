from collections import defaultdict

DIRECTIONS = [(UP := (-1, 0)), (RIGHT := (0, 1)), (DOWN := (1, 0)), (LEFT := (0, -1))]
Dir = Pos = tuple[int, int]
Board = list[str]


def next_dir(cur_dir: Dir) -> Dir:
    return {UP: RIGHT, RIGHT: DOWN, DOWN: LEFT, LEFT: UP}[cur_dir]


def get_dir(board: Board, guard_pos: Pos) -> Dir:
    return {"^": UP, "v": DOWN, ">": RIGHT, "<": LEFT}[board[guard_pos[0]][guard_pos[1]]]


def in_range(board: Board, pos: Pos) -> bool:
    return pos[0] in range(len(board)) and pos[1] in range(len(board[0]))


def does_it_loop(guard_pos: Pos, cur_dir: Dir, board: Board, visited: dict[Pos, set], new_block: Pos) -> bool:
    new_visited = defaultdict(set)
    while True:
        new_pos = (guard_pos[0] + cur_dir[0], guard_pos[1] + cur_dir[1])
        if not in_range(board, new_pos):
            return False

        if new_pos == new_block or board[new_pos[0]][new_pos[1]] == "#":
            cur_dir = next_dir(cur_dir)
        else:
            guard_pos = new_pos

        if cur_dir in new_visited[guard_pos] or cur_dir in visited.get(guard_pos, set()):
            return True
        new_visited[guard_pos].add(cur_dir)


def part1(board: Board, guard_pos: Pos) -> int:
    cur_dir = get_dir(board, guard_pos)
    visited = {guard_pos}
    while True:
        new_pos = (guard_pos[0] + cur_dir[0], guard_pos[1] + cur_dir[1])
        if not in_range(board, new_pos):
            return len(visited)
        if board[new_pos[0]][new_pos[1]] == "#":
            cur_dir = next_dir(cur_dir)
        else:
            guard_pos = new_pos
            visited.add(new_pos)


def part2(board: Board, guard_pos: Pos) -> int:
    cur_dir = get_dir(board, guard_pos)
    places_that_can_be_blocked = set()
    visited = defaultdict(set)
    visited[guard_pos].add(cur_dir)
    while True:
        new_pos = (guard_pos[0] + cur_dir[0], guard_pos[1] + cur_dir[1])
        if not in_range(board, new_pos):
            return len(places_that_can_be_blocked)
        if board[new_pos[0]][new_pos[1]] == "#":
            cur_dir = next_dir(cur_dir)
        else:
            if (
                new_pos not in visited
                and new_pos not in places_that_can_be_blocked
                and does_it_loop(guard_pos, next_dir(cur_dir), board, visited, new_pos)
            ):
                places_that_can_be_blocked.add(new_pos)
            guard_pos = new_pos
        visited[guard_pos].add(cur_dir)


def main():
    with open("inputs/day06.txt") as f:
        board = f.read().split('\n')
    guard_pos = next((r, c) for r, row in enumerate(board) for c, x in enumerate(row) if x in "^v><")
    print(part1(board, guard_pos))
    print(part2(board, guard_pos))


if __name__ == '__main__':
    main()
