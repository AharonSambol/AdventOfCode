from functools import lru_cache

PieceType = tuple[tuple[str, ...], ...]


def place(board: list[list[bool]], pos: tuple[int, int], piece: PieceType, to_place: bool) -> None:
    for r, row in enumerate(piece):
        for c, item in enumerate(row):
            if item == "#":
                board[pos[0] + r][pos[1] + c] = to_place


def fits(board: list[list[bool]], pos: tuple[int, int], piece: PieceType) -> bool:
    try:
        for r, row in enumerate(piece):
            for c, item in enumerate(row):
                if item == "#" and board[pos[0] + r][pos[1] + c]:
                    return False
    except IndexError:
        return False
    return True


@lru_cache
def get_orientations(piece: PieceType) -> list[PieceType]:
    res = []
    orig_piece = piece
    for flip in [True, False]:
        for rotation in range(4):
            piece = orig_piece
            if flip:
                piece = piece[::-1]
            for _ in range(rotation):
                piece = tuple(tuple(x) for x in zip(*piece))[::-1]
            if piece not in res:
                res.append(piece)
    return res


def can_fit(
    pieces: list[PieceType],
    board: list[list[bool]],
    presents: list[int],
    starting_pos: tuple[int, int]
) -> bool:
    if sum(presents) == 0:
        return True
    hashtags_left = sum(
        sum(item == '#' for row in pieces[i] for item in row) * amount
        for i, amount in enumerate(presents)
    )
    for r in range(starting_pos[0], min(starting_pos[0] + 3, len(board) - 2)):
        for c in range(starting_pos[1] if r == starting_pos[0] else 0, len(board[0]) - 2):
            if (len(board) - r) * len(board[0]) - c < hashtags_left:
                return False

            for present, amount in enumerate(presents):
                if amount == 0:
                    continue
                for piece in get_orientations(pieces[present]):
                    if fits(board, (r, c), piece):
                        place(board, (r, c), piece, True)
                        presents[present] -= 1
                        next_pos = (r, c + 1) if c < len(board[0]) - 3 else (r + 1, 0)
                        if can_fit(pieces, board, presents, next_pos):
                            return True
                        presents[present] += 1
                        place(board, (r, c), piece, False)
    return False


def main():
    with open("inputs/day12.txt") as f:
        *pieces, temp_requirements = f.read().split("\n\n")
        pieces = [tuple(tuple(row) for row in piece.split(":\n")[1].split("\n")) for piece in pieces]
        requirements = []
        for requirement in temp_requirements.split("\n"):
            board, presents = requirement.split(": ")
            requirements.append(([int(x) for x in board.split("x")], [int(x) for x in presents.split(" ")]))
        print(sum(
            can_fit(
                pieces,
                [[False] * board_size[0] for _ in range(board_size[1])],
                presents,
                (0, 0)
            )
            for board_size, presents in requirements
        ))


if __name__ == '__main__':
    main()
