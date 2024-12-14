class SetMock:
    def __contains__(self, item):
        return False

    def add(self, other):
        pass


def get_trail_score(
    board: list[list[int]], r: int, c: int, visited: set[tuple[int, int]]
) -> int:
    if board[r][c] == 9:
        return 1
    res = 0
    for rd, cd in [[1, 0], [0, 1], [0, -1], [-1, 0]]:
        if (
            (r + rd, c + cd) not in visited
            and r + rd in range(len(board))
            and c + cd in range(len(board[0]))
            and board[r + rd][c + cd] == board[r][c] + 1
        ):
            visited.add((r + rd, c + cd))
            res += get_trail_score(board, r + rd, c + cd, visited)
    return res


def solve(board: list[list[int]], is_part1: bool) -> int:
    return sum(
        get_trail_score(board, r, c, set() if is_part1 else SetMock())
        for r, row in enumerate(board)
        for c, x in enumerate(row)
        if x == 0
    )


def main():
    with open("inputs/day10.txt") as f:
        board = [[int(x) for x in line] for line in f.read().split("\n")]
    print(solve(board, True))
    print(solve(board, False))


if __name__ == "__main__":
    main()
