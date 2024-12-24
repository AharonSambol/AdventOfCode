from typing import Iterable

DIRS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Pos = tuple[int, int]


def find_pos(board: list[list[str]], looking_for: str) -> tuple[int, int]:
    return next((r, c) for r, row in enumerate(board) for c, x in enumerate(row) if x == looking_for)


def is_valid_pos(board: list[list[str]], pos: Pos) -> bool:
    try:
        return board[pos[0]][pos[1]] != '#'
    except IndexError:
        return False


def traverse(board: list[list[str]], start: Pos) -> Iterable[tuple[Pos, int]]:
    queue = [(start, 0)]
    visited = set()
    while True:
        pos, cost = queue.pop(0)
        for dr, dc in DIRS:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if is_valid_pos(board, new_pos) and new_pos not in visited:
                visited.add(new_pos)
                queue.append((new_pos, cost + 1))
                yield new_pos, cost + 1


def get_distances_from_end(base: int, board: list[list[str]], end: Pos, must_save: int) -> dict[Pos, int]:
    distances_from_end = {}
    for pos, cost in traverse(board, end):
        if cost > base - must_save:
            break
        distances_from_end[pos] = cost
    return distances_from_end


def solve(board: list[list[str]], start: Pos, end: Pos) -> int:
    for pos, cost in traverse(board, start):
        if pos == end:
            return cost


def solve_with_cheat(board: list[list[str]], start: Pos, end: Pos, cheat_len: int, must_save: int) -> int:
    base = solve(board, start, end)
    distances_from_end = get_distances_from_end(base, board, end, must_save)
    res = set()
    for pos, cost in traverse(board, start):
        if cost >= base - must_save:
            break
        for rd in range(-cheat_len, cheat_len + 1):
            has_moved = abs(rd)
            for cd in range(-cheat_len + has_moved, cheat_len - has_moved + 1):
                new_pos = (pos[0] + rd, pos[1] + cd)
                cheat_distance = has_moved + abs(cd)
                if cost + cheat_distance + distances_from_end.get(new_pos, base) <= base - must_save:
                    res.add((pos, new_pos))
    return len(res)


def main():
    with open('inputs/day20.txt') as f:
        board = [list(x) for x in f.read().split('\n')]
    start = find_pos(board, 'S')
    end = find_pos(board, 'E')
    print(solve_with_cheat(board, start, end, 2, 100))
    print(solve_with_cheat(board, start, end, 20, 100))


if __name__ == '__main__':
    main()
