import itertools
import re
import time
from collections import defaultdict
from functools import reduce

WIDTH = 101
HEIGHT = 103
WIDTH_MIDDLE = WIDTH // 2
HEIGHT_MIDDLE = HEIGHT // 2


def calc_new_posses(robots: list[list[int]], seconds: int) -> list[tuple[int, int]]:
    return [
        ((robot[1] + robot[3] * seconds) % HEIGHT, (robot[0] + robot[2] * seconds) % WIDTH)
        for robot in robots
    ]


def part1(robots: list[list[int]]) -> int:
    quarters = [0] * 4
    for robot in calc_new_posses(robots, 100):
        if robot[0] == HEIGHT_MIDDLE or robot[1] == WIDTH_MIDDLE:
            continue
        index = (robot[1] > WIDTH_MIDDLE) + (robot[0] > HEIGHT_MIDDLE) * 2
        quarters[index] += 1
    return reduce(lambda a, b: a * b, quarters, 1)


def part2(robots: list[list[int]]) -> None:
    for second in itertools.count():
        new_posses = calc_new_posses(robots, second)
        posses_dict = defaultdict(set)
        for r, c in new_posses:
            posses_dict[r].add(c)
        if sum(len(x) > 10 for x in posses_dict.values()) > 15:
            print('----------', second, '----------')
            for r in range(HEIGHT):
                for c in range(WIDTH):
                    print('█' if (r, c) in new_posses else ' ', end='')
                print()
            time.sleep(0.5)


def main():
    with open("inputs/day14.txt") as f:
        content = f.read().split('\n')
        robots = [[int(x) for x in re.findall(r"-?\d+", line)] for line in content]
    print(part1(robots))
    print(part2(robots))


if __name__ == '__main__':
    main()
