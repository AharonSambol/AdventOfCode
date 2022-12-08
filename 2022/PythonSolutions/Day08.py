from functools import reduce


def val(grid, r, c, part1):
    rgrid = list(zip(*grid))
    dirs = (grid[r][:c][::-1], grid[r][c + 1:], rgrid[c][:r][::-1], rgrid[c][r + 1:])
    if part1:
        return min(max(x or [-1]) for x in dirs) < grid[r][c]
    len_until_limit = lambda limit, it: next((i + 1 for i, x in enumerate(it) if x >= limit), len(it))
    return reduce(lambda x, y: x * y, (len_until_limit(grid[r][c], dr) for dr in dirs))


with open("../Inputs/InputDay08.txt") as file:
    m = [list(int(x) for x in line.rstrip()) for line in file]
    print(sum(val(m, r, c,  True) for r in range(len(m)) for c in range(len(m[0]))))
    print(max(val(m, r, c, False) for r in range(len(m)) for c in range(len(m[0]))))
