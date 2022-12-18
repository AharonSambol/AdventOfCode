#! not serious code, just trying to be as few lines as possible
with open("../Inputs/InputDay18.txt") as file:
    grid = {(*map(int, line.split(',')),) for line in file.read().split('\n')}
    print(sum(p not in grid for x, y, z in grid for i in (1, -1) for p in ((x, y, z+i), (x, y+i, z), (x+i, y, z))))
    q, seen, checked_posses = [pos := ((mx := max(grid, key=lambda p: p[0]))[0], mx[1], mx[2] + 1)], 0, {pos}
    while q:
        x, y, z = q.pop()
        if any((x + xx, y + yy, z + zz) in grid for xx in (-1, 0, 1) for yy in (-1, 0, 1) for zz in (-1, 0, 1)):
            for new_point in (p for i in (1, -1) for p in ((x, y, z+i), (x, y+i, z), (x+i, y, z))):
                if new_point not in checked_posses and seen == (seen := seen + (new_point in grid)):
                    checked_posses, q = checked_posses | {new_point}, q + [new_point]
    print(seen)
