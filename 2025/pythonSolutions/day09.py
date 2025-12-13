from typing import cast


def valid_rectangle(point: tuple[int, int], other_point: tuple[int, int], outside_border: set[tuple[int, int]]) -> bool:
    for c in range(min(point[1], other_point[1]), max(point[1], other_point[1])):
        for r in [point[0], other_point[0]]:
            if (r, c) in outside_border:
                return False
    for r in range(min(point[0], other_point[0]), max(point[0], other_point[0])):
        for c in [point[1], other_point[1]]:
            if (r, c) in outside_border:
                return False
    return True


def get_outside_border(border: set[tuple[int, int]], point: tuple[int, int]) -> set[tuple[int, int]]:
    points_to_check = [point]
    outside_border = {point}
    while points_to_check:
        point = points_to_check.pop()
        for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
            new_point = (point[0] + d[0], point[1] + d[1])
            if new_point in border or new_point in outside_border:
                continue
            for d in [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                if (new_point[0] + d[0], new_point[1] + d[1]) in border:
                    outside_border.add(new_point)
                    points_to_check.append(new_point)
                    break
    return outside_border


def part1(points: list[tuple[int, int]]) -> int:
    max_rectangle = 0
    for i, point in enumerate(points):
        for other_point in points[i + 1:]:
            max_rectangle = max(max_rectangle,
                                (abs(point[0] - other_point[0]) + 1) * (abs(point[1] - other_point[1]) + 1))
    return max_rectangle


def part2(points: list[tuple[int, int]]) -> int:
    border = set()
    for start, end in zip(points, points[1:] + [points[0]]):
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
                border.add((x, y))
    top_point = min(border, key=lambda x: x[0])
    outside_border = get_outside_border(border, (top_point[0] - 1, top_point[1]))

    possible_rectangles = []
    for i, point in enumerate(points):
        for other_point in points[i + 1:]:
            possible_rectangles.append((point, other_point, (abs(point[0] - other_point[0]) + 1) * (abs(point[1] - other_point[1]) + 1)))

    while True:
        i, (point, other_point, size) = max(enumerate(possible_rectangles), key=lambda x: x[1][2])
        if valid_rectangle(point, other_point, outside_border):
            return size
        else:
            possible_rectangles[i] = (0, 0, 0)


def main():
    with open("inputs/day09.txt") as f:
        points = cast(
            list[tuple[int, int]],
            [tuple([int(x) for x in line.split(",")]) for line in f.read().split("\n")]
        )
        print("part1:", part1(points))
        print("part2:", part2(points))


if __name__ == '__main__':
    main()