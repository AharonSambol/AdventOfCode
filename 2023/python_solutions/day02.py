import re
from functools import reduce


def get_minimums(line):
    return {
        color: max(map(int, re.findall(r'(\d+) ' + color, line)))
        for color in ['red', 'green', 'blue']
    }


with open("../inputs/day02.txt") as file:
    lines = file.readlines()
    print(
        sum(
            int(re.search(r'\d+', line).group())
            for line in lines
            if all(num <= {'red': 12, 'green': 13, 'blue': 14}[color] for color, num in get_minimums(line).items())
        )
    )
    print(sum(reduce(lambda a, b: a * b, get_minimums(line).values()) for line in lines))
