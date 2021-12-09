import math

neighbors = [(1, 0), (-1, 0), (0, 1), (0, -1)]
in_range = lambda r, c: all(p in range(len(ipt)) for p in [r, c])
is_bigger = lambda r, c, val: not in_range(r, c) or ipt[r][c] > val


def day9():
    ans, basins = 0, []
    for r, row in enumerate(ipt):
        for c, val in enumerate(row):
            if all(is_bigger(r + r_add, c + c_add, val) for r_add, c_add in neighbors):
                ans += 1 + val  # part1
                basins.append(explore_basin(r, c, {(r, c)}))    # part2
    print(f"part1: { ans }")
    print(f"part2: { math.prod(sorted(basins, reverse=True)[:3]) }")


def explore_basin(r, c, visited):
    for r_add, c_add in neighbors:
        if in_range((new_r := r + r_add), (new_c := c + c_add)):
            if (new_r, new_c) not in visited and 9 != ipt[new_r][new_c] > ipt[r][c]:
                visited.add((new_r, new_c))
                explore_basin(new_r, new_c, visited)
    return len(visited)


if __name__ == '__main__':
    with open("day9") as input_file:
        ipt = [[int(num) for num in x.strip()] for x in input_file.readlines()]
    day9()
