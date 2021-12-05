def inclusive_range(start, end):
    direction = -1 if start > end else 1
    return list(range(start, end + direction, direction))


def day5(part1):
    with open("day5") as input_file:
        input_data = input_file.readlines()
        d = {}
        for line in input_data:
            (x1, y1), (x2, y2) = (map(int, point.split(',')) for point in line.strip().split(' -> '))
            if part1 and x1 != x2 and y1 != y2:
                continue
            xs, ys = inclusive_range(x1, x2), inclusive_range(y1, y2)
            ln = max(len(xs), len(ys))
            xs.extend([x1] * (ln - len(xs)))    # so that zip doesn't stop early
            ys.extend([y1] * (ln - len(ys)))
            for x, y in zip(xs, ys):
                d[(x, y)] = d.get((x, y), 0) + 1
        return sum(v >= 2 for v in d.values())


print(f'part1 solution: { day5(True)  }')
print(f'part2 solution: { day5(False) }')
