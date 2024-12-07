from collections import Counter


def part1(left_nums: list[int], right_nums: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(sorted(left_nums), sorted(right_nums)))


def part2(left_nums: list[int], right_nums: list[int]) -> int:
    counter = Counter(right_nums)
    return sum(num * counter[num] for num in left_nums)


def main():
    with open('inputs/day01.txt') as f:
        nums = [int(x) for x in f.read().split()]
    print(part1(nums[::2], nums[1::2]))
    print(part2(nums[::2], nums[1::2]))


if __name__ == '__main__':
    main()
