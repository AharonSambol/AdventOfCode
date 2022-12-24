# purposefully made this hard on myself by trying to make a O(n) memory solution
from dataclasses import dataclass
import re


SIDE_SIZE = 50
rotate_down = {'u': 'b', 'f': 'u', 'r': 'r', 'l': 'l', 'b': 'd', 'd': 'f'}
rotate_left = {'u': 'u', 'd': 'd', 'r': 'b', 'b': 'l', 'l': 'f', 'f': 'r'}
rotate_up    = {v: k for k, v in rotate_down.items()}
rotate_right = {v: k for k, v in rotate_left.items()}
rotation_maps = {'down': rotate_down, 'left': rotate_left, 'up': rotate_up, 'right': rotate_right}
rotation_opposites = {'down': 'up', 'left': 'right', 'up': 'down', 'right': 'left'}
angle_to_change = {0: (0, 1), 90: (1, 0), 180: (0, -1), 270: (-1, 0)}


@dataclass
class Side:
    pos: (int, int)
    top_bordering_with: str


def rotate_cube(cube, rotation_dir):
    new_cube = [(k, cube[rotation_maps[rotation_dir][k]]) for k, v in cube.items()]
    for k, v in new_cube:
        if v:
            v.top_bordering_with = rotation_maps[rotation_opposites[rotation_dir]][v.top_bordering_with]
        cube[k] = v


def fold(board):
    cube = {x: None for x in 'fburld'}
    sides = {}
    top_side = top_side_pos = None
    for r in range(len(board) //  SIDE_SIZE):
        for c in range(len(board[r *  SIDE_SIZE]) //  SIDE_SIZE):
            if board[r *  SIDE_SIZE][c *  SIDE_SIZE] == ' ':
                continue
            sides[(r, c)] = Side((r, c), 'u')
            top_side = top_side or sides[top_side_pos := (r, c)]
    cube['f'] = top_side
    add_to_cube(cube, sides, *top_side_pos)
    return cube


def add_to_cube(cube, sides, r, c):
    for dr, neighbor_pos in (('left', (r, c + 1)), ('right', (r, c - 1)), ('up', (r + 1, c)), ('down', (r - 1, c))):
        if neighbor_pos not in sides or cube[rotation_maps[dr]['f']]:
            continue
        rotate_cube(cube, dr)
        cube['f'] = sides[neighbor_pos]
        add_to_cube(cube, sides, *neighbor_pos)
        rotate_cube(cube, rotation_opposites[dr])


def move(board, pos, dr, instruction, cube, part1):
    if instruction in ['R', 'L']:
        return pos, (dr + {'R': 90, 'L': -90}[instruction]) % 360, cube
    for _ in range(int(instruction)):
        change = angle_to_change[dr]
        r, c = new_pos = pos[0] + change[0], pos[1] + change[1]
        if part1:
            if not (0 <= r < len(board) and 0 <= c < len(board[r])) or board[r][c] == ' ':
                r, c = r - change[0], c - change[1]
                while 0 <= r < len(board) and 0 <= c < len(board[r]) and board[r][c] != ' ':
                    new_pos = (r, c)
                    r, c = r - change[0], c - change[1]
            if board[new_pos[0]][new_pos[1]] == '#':
                break
            pos = new_pos
        else:
            new_dr, new_cube, reverse = dr, cube, []
            if not (0 <= r < SIDE_SIZE and 0 <= c < SIDE_SIZE):
                new_pos = [x % SIDE_SIZE for x in new_pos]
                change = 'down' if r < 0 else 'up' if r >= SIDE_SIZE else 'right' if c < 0 else 'left'
                rotate_cube(cube, change)
                reverse.append(rotation_opposites[change])
                while new_cube['f'].top_bordering_with != 'u':
                    for rotate in ('down', 'left', 'up'):   # rotate on other axis
                        rotate_cube(new_cube, rotate)
                        reverse.append(rotation_opposites[rotate])
                    new_pos = (SIDE_SIZE - 1 - new_pos[1], new_pos[0])
                    new_dr = (new_dr - 90) % 360
            tile_pos = [x * SIDE_SIZE for x in new_cube['f'].pos]
            if board[tile_pos[0] + new_pos[0]][tile_pos[1] + new_pos[1]] == '#':
                for x in reverse[::-1]:
                    rotate_cube(cube, x)
                break
            cube, pos, dr = new_cube, new_pos, new_dr
    return pos, dr, cube


def main():
    with open("../Inputs/InputDay22.txt") as file:
        board, instructions = file.read().split('\n\n')
        instructions = re.findall(r'(\d+|R|L)', instructions)
        board = [list(row) for row in board.split('\n')]
        cube = fold(board)
        pos, dr = (0, board[0].index('.')), 0
        pos2, dr2 = (0, 0), 0
        for instruction in instructions:
            pos, dr, _ = move(board, pos, dr, instruction, None, True)
            pos2, dr2, cube = move(board, pos2, dr2, instruction, cube, False)
        print('part1:', 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + dr // 90)
        cur_face = [SIDE_SIZE * x for x in cube['f'].pos]
        print('part2:', 1000 * (pos2[0] + 1 + cur_face[0]) + 4 * (pos2[1] + 1 + cur_face[1]) + dr2 // 90)


if __name__ == '__main__':
    main()