import math
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def solve(stone: int, iterations: int) -> int:
    if iterations == 0:
        return 1
    if stone == 0:
        return solve(1, iterations - 1)
    log10 = int(math.log10(stone)) + 1
    if log10 & 1 == 0:
        left, right = divmod(stone, 10 ** (log10 >> 1))
        return solve(left, iterations - 1) + solve(right, iterations - 1)
    return solve(stone * 2024, iterations - 1)


def main():
    with open('inputs/day11.txt') as f:
        stones = [int(x) for x in f.read().split()]
    print(sum(solve(stone, 75) for stone in stones))


if __name__ == '__main__':
    main()
