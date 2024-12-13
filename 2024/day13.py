import re
from decimal import Decimal


def solve(is_part2: bool) -> int:
    res = 0
    for nums in chunks:
        a_x, a_y, b_x, b_y, prize_x, prize_y = nums
        if is_part2:
            prize_x += 10000000000000
            prize_y += 10000000000000
        eq_left = b_x / a_x - b_y / a_y
        eq_right = prize_x / a_x - prize_y / a_y
        b = eq_right / eq_left
        a = (prize_x - (b_x * b)) / a_x
        a, b = [x.quantize(Decimal('0.001')) for x in [a, b]]
        if a == int(a) and b == int(b):
            res += int(a * 3 + b)
    return res


with open('inputs/day13.txt') as f:
    chunks = [[Decimal(x) for x in re.findall(r'\d+', chunk)] for chunk in f.read().split('\n\n')]
    print(solve(False))
    print(solve(True))
