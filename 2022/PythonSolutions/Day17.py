with open("../Inputs/InputDay17.txt") as file:
    dirs = file.readline()

tiles = (((0, 0), (1, 0), (2, 0), (3, 0)),
         ((1, 0), (0, 1), (1, 1), (2, 1), (1, 2)),
         ((0, 0), (1, 0), (2, 0), (2, 1), (2, 2)),
         ((0, 0), (0, 1), (0, 2), (0, 3)),
         ((0, 0), (0, 1), (1, 0), (1, 1)))


def place_tile(board, tile, offset_x, offset_y):
    for x, y in tile:
        board.add((x + offset_x, y + offset_y))

def is_valid(board, tile, offset_x, offset_y):
    return all((x + offset_x, y + offset_y) not in board for x, y in tile)

def can_skip(dct, starting_pos, d, piece_num, goal, board):
    if piece_num != 0 and piece_num % 3 == 0:
        moves = piece_num // 3
        (height_at_2thirds, d_pos) = dct[moves * 2]
        (height_at_third, d_pos2)  = dct[moves]
        height_at_repeat = cur_height = starting_pos - 3
        if d_pos == d_pos2 == d % len(dirs) and cur_height - height_at_2thirds == height_at_2thirds - height_at_third:
            growth = cur_height - height_at_2thirds
            res = height_at_third + growth * (goal // moves - 1)
            for i in range(1, goal % moves):
                _, starting_pos, d = fall_piece(piece_num + i, board, dct, starting_pos, d, goal)
            return res + starting_pos - 3 - height_at_repeat, starting_pos, d
    return False

def fall_piece(piece_num, board, dct, starting_pos, d, goal):
    tile = tiles[piece_num % len(tiles)]
    biggest_x = max(tile, key=lambda p: p[0])[0]
    off_set_y, off_set_x = starting_pos, 2
    while True:
        if dirs[d] == '>':
            if off_set_x + biggest_x < 6 and is_valid(board, tile, off_set_x + 1, off_set_y):
                off_set_x += 1
        elif off_set_x > 0 and is_valid(board, tile, off_set_x - 1, off_set_y):
            off_set_x -= 1
        d = (d + 1) % len(dirs)
        if not is_valid(board, tile, off_set_x, off_set_y - 1):
            place_tile(board, tile, off_set_x, off_set_y)
            starting_pos = max(starting_pos, 4 + off_set_y + max(tile, key=lambda p: p[1])[1])
            dct.append((starting_pos - 3, d % len(dirs)))
            if res := can_skip(dct, starting_pos, d, piece_num, goal, board):
                return res
            return starting_pos - 3 if piece_num + 1 == goal else False, starting_pos, d
        off_set_y -= 1


def main(goal):
    board = {(x, -1) for x in range(7)}
    dct, starting_pos, d = [], 3, 0
    for piece_num in range(goal):
        res, starting_pos, d = fall_piece(piece_num, board, dct, starting_pos, d, goal)
        if res:
            return res

if __name__ == '__main__':
    print('part1:', main(2022))
    print('part2:', main(1_000_000_000_000))
