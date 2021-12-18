import re


def day17(range_x, range_y):
    max_x, min_y = range_x[1], range_y[0]
    min_x = sm = max_y = amount = 0
    while sm + min_x + 1 <= range_x[0]:
        sm += (min_x := min_x + 1)
    for y in range(min_y, 1000):
        for x in range(min_x, max_x+1):
            success, res = hit(x, y, range_x, range_y)
            max_y, amount = max(max_y, res), amount + success
    return max_y, amount


def hit(x, y, range_x, range_y):
    pos_x = pos_y = max_y = 0
    while pos_x <= range_x[1] and pos_y >= range_y[0]:
        pos_x, pos_y = pos_x + x, pos_y + y
        x, max_y, y = max(0, x-1), max(max_y, pos_y), y - 1
        if range_x[0] <= pos_x <= range_x[1] and range_y[0] <= pos_y <= range_y[1]:
            return 1, max_y
    return 0, 0


if __name__ == '__main__':
    with open("day17") as input_file:
        x_range, y_range = [tuple(map(int, rng)) for rng in re.findall(r'(-?\d+)\.\.(-?\d+)', input_file.read())]
    print(day17(x_range, y_range))
