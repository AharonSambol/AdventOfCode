from functools import partial
from collections import Counter


def calc_type(hand, is_part1):
    counter = Counter(hand)
    max_card = max(counter.items(), key=lambda x: x[1] * (x[0] != 'J'))[0]
    if not is_part1:
        counter[max_card] += counter.pop('J', 0) * (max_card != 'J')
    return max(counter.values()) * 10 + list(counter.values()).count(2)     # 10 is just a rand big number (more than the amount of possible 2s)


def calc_val(line, is_part1):
    digits = '23456789TJQKA' if is_part1 else 'J23456789TQKA'
    hand = line.split()[0]
    hand_val = sum(digits.index(digit) * len(digits) ** i for i, digit in enumerate(hand[::-1]))
    return hand_val + (calc_type(hand, is_part1) * len(digits) ** len(hand))


with open("../inputs/day07.txt") as file:
    print(sum(
        rank * int(line.split()[1].strip())
        for rank, line in enumerate(sorted(file.readlines(), key=partial(calc_val, is_part1=False)), start=1)
    ))
