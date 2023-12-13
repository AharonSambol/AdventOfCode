import re
import time
from functools import lru_cache


def is_expected(res, expected_ones, expected_zeros, ln):
    if res | expected_ones != res:
        return False
    res = (1 << ln) - 1 - res   # bin not
    return res | expected_zeros == res


@lru_cache
def count_permutations(bits_left, numbers, expected_ones, expected_zeros, number_left_sum):
    if bits_left == number_left_sum:
        res = 0
        for num in numbers:
            res = ((res + 1) << (num + 1)) - 2
        res >>= 1
        bin_ln = (1 << number_left_sum) - 1
        return is_expected(res, expected_ones & bin_ln, expected_zeros & bin_ln, number_left_sum)
    answer = 0
    if expected_ones & (1 << (bits_left - 1)) == 0:
        answer += count_permutations(bits_left - 1, numbers, expected_ones, expected_zeros, number_left_sum)
    left_after_num = bits_left - numbers[0]
    if 0 == expected_zeros & (((1 << numbers[0]) - 1) << left_after_num) == expected_ones & (1 << (left_after_num - 1)):
        if len(numbers) == 1:
            return answer + (expected_ones & ((1 << left_after_num) - 1) == 0)
        answer += count_permutations(
            left_after_num - 1, numbers[1:], expected_ones, expected_zeros, number_left_sum - numbers[0] - 1
        )
    return answer


def count_possible_solutions(line, is_part1):
    line, *numbers = re.findall(r'([.#?]+|\d+)', line)
    numbers = [int(num) for num in numbers]
    if not is_part1:
        line, numbers = '?'.join([line] * 5), numbers * 5
    expected_zeros = expected_ones = 0
    for char in line:
        expected_ones = (expected_ones << 1) + (char == '#')
        expected_zeros = (expected_zeros << 1) + (char == '.')
    return count_permutations(len(line), tuple(numbers), expected_ones, expected_zeros, sum(numbers) + len(numbers) - 1)


for is_part1 in [True, False]:
    with open("../inputs/day12.txt") as file:
        start = time.time()
        print(sum(count_possible_solutions(line, is_part1) for line in file))
        print(time.time() - start)
