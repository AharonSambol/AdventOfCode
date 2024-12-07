from typing import TextIO, Iterator

Equation = tuple[int, list[int]]


def parse_input(file: TextIO) -> Iterator[Equation]:
    for line in file.read().split("\n"):
        res, nums = line.split(": ")
        nums = [int(x) for x in nums.split(" ")]
        yield int(res), nums


def can_get_to_sum(goal: int, cur: int, nums: list[int]) -> bool:
    if not nums:
        return cur == goal
    return (
        can_get_to_sum(goal, cur + nums[0], nums[1:])
        or can_get_to_sum(goal, cur * nums[0], nums[1:])
        # For part2:
        or can_get_to_sum(goal, int(f"{cur}{nums[0]}"), nums[1:])
    )


def solve(equations: Iterator[Equation]) -> int:
    res = 0
    for goal, nums in equations:
        if can_get_to_sum(goal, nums[0], nums[1:]):
            res += goal
    return res


def main():
    with open('inputs/day07.txt') as f:
        equations = parse_input(f)
        print(solve(equations))


if __name__ == '__main__':
    main()
