import copy
import itertools

EMPTY = '.'
ROBOT = '@'
WALL = '#'
BOX = 'O'
BOXL = '['
BOXR = ']'

INSTRUCTION_TO_DIR = {
    '^': (-1, 0),
    'v': (1, 0),
    '<': (0, -1),
    '>': (0, 1),
}
PART_2_MAPPING = {
    EMPTY: [EMPTY, EMPTY],
    ROBOT: [ROBOT, EMPTY],
    WALL: [WALL, WALL],
    BOX: [BOXL, BOXR]
}


def get_starting_pos(board: list[list[str]]) -> tuple[int, int]:
    return next((r, c) for r, row in enumerate(board) for c, x in enumerate(row) if x == ROBOT)


def count_result(board: list[list[str]], box: str) -> int:
    return sum(100 * r + c for r, row in enumerate(board) for c, x in enumerate(row) if x == box)


def part1(board: list[list[str]], instructions: list[tuple[int, int]]) -> int:
    pos = get_starting_pos(board)
    for instruction in instructions:
        end_point = new_pos = pos[0] + instruction[0], pos[1] + instruction[1]
        while board[end_point[0]][end_point[1]] == BOX:
            end_point = end_point[0] + instruction[0], end_point[1] + instruction[1]
        if board[end_point[0]][end_point[1]] == WALL:
            continue
        board[end_point[0]][end_point[1]] = BOX
        board[new_pos[0]][new_pos[1]] = ROBOT
        board[pos[0]][pos[1]] = EMPTY
        pos = new_pos
    return count_result(board, BOX)


def can_move(board: list[list[str]], pos: tuple[int, int], direction: tuple[int, int]) -> bool:
    r, c = pos[0] + direction[0], pos[1] + direction[1]
    if board[r][c] in [BOXL, BOXR]:
        return (
            can_move(board, (r, c), direction)
            and (
                not direction[0]
                or can_move(board, (r, c + (1 if board[r][c] == BOXL else -1)), direction)
            )
        )
    return board[r][c] == EMPTY


def move(board: list[list[str]], pos: tuple[int, int], direction: tuple[int, int]) -> None:
    r, c = pos[0] + direction[0], pos[1] + direction[1]
    if board[r][c] in [BOXL, BOXR]:
        other_c = c + (1 if board[r][c] == BOXL else -1)
        move(board, (r, c), direction)
        if direction[0]:
            move(board, (r, other_c), direction)
    board[r][c] = board[pos[0]][pos[1]]
    board[pos[0]][pos[1]] = EMPTY


def part2(board: list[list[str]], instructions: list[tuple[int, int]]) -> int:
    board = [list(itertools.chain.from_iterable(PART_2_MAPPING[x] for x in row)) for row in board]
    pos = get_starting_pos(board)
    for instruction in instructions:
        if can_move(board, pos, instruction):
            move(board, pos, instruction)
            pos = pos[0] + instruction[0], pos[1] + instruction[1]
    return count_result(board, BOXL)


def main():
    with open('inputs/day15.txt') as f:
        board, instructions = f.read().split('\n\n')
    board = [list(row) for row in board.split('\n')]
    instructions = [INSTRUCTION_TO_DIR[x] for x in instructions.replace('\n', '')]
    print(part1(copy.deepcopy(board), instructions))
    print(part2(board, instructions))


if __name__ == '__main__':
    main()
