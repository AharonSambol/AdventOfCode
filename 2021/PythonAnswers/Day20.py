def part1(mp, lookup, row_ln, col_ln, default, non_default):
    zero, nine = lookup[0], lookup[int('1' * 9, 2)]
    for _ in range(50):
        next_default =  zero if default == '.' else nine
        new_map, checked = set(), set()
        for pos in mp:
            for r in range(-1, 2):
                for c in range(-1, 2):
                    check_pos = (pos[0] + r, pos[1] + c)
                    if check_pos in checked:
                        continue
                    checked.add(check_pos)
                    if get_bit(mp, check_pos[0], check_pos[1], lookup, default, non_default, next_default):
                        new_map.add(check_pos)
        default = next_default
        non_default = {'#': '.', '.': '#'}[default]

        mp = new_map
    print(len(mp))


def get_bit(mp, row, col, lookup, default, non_default, next_default):
    pos = ''
    for r in range(-1, 2):
        for c in range(-1, 2):
            pos += {'#': '1', '.': '0'}[non_default if (row + r, col + c) in mp else default]
    return lookup[int(pos, 2)] != next_default

with open('/home/aharonsambol/code/advent/day20.txt') as input_file:
    lookup, arr = input_file.read().split('\n\n')
arr = [line.strip() for line in arr.split('\n')]
mp = {(row, col) for row in range(len(arr)) for col in range(len(arr[0])) if arr[row][col] == '#'}
part1(mp, lookup, len(arr), len(arr[0]), '.', '#')
