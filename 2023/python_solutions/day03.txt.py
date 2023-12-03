import re
from collections import defaultdict

with open("../inputs/day03.txt") as file:
    schematic = ['.' * 200, *(f'.{x.strip()}.' for i, x in enumerate(file)), '.' * 200]

gears, res = defaultdict(list), 0
for row in range(len(schematic)):
    for number in re.finditer(r'\d+', schematic[row]):
        group = ''.join(schematic[r][number.start() - 1: number.end() + 1] for r in [row - 1, row, row + 1])
        group_width = len(number.group()) + 2
        if (pos := group.find('*')) != -1:
            gear_pos = row - 1 + (pos // group_width), number.start() - 1 + pos % group_width
            gears[gear_pos].append(int(number.group()))
        if not re.fullmatch(rf'\.{{{group_width + 1}}}{number.group()}\.{{{group_width + 1}}}', group):
            res += int(number.group())
print(res)
print(sum(lst[0] * lst[1] for lst in gears.values() if len(lst) == 2))
