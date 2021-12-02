import re
from collections import Counter


with open("day2") as input_file:
    inpt = input_file.readlines()
    # part 01
    c = Counter()
    for line in inpt:
        instruction, amount = line.split()
        c[instruction] += int(amount)
    print(c['forward'] * (c['down'] - c['up']))

    # part 01 regex solution
    text = ''.join(inpt).replace('down ', '+').replace('up ', '-')
    forward = sum(map(int, re.findall(r'(?<=forward )\d+', text)))
    depth = sum(map(int, re.findall(r'[+-]\d+', text)))
    print(depth * forward)

    # part 02
    aim = depth = hor = 0
    for line in inpt:
        instruction, amount = line.split()
        amount = int(amount)
        if instruction == 'forward':
            hor += amount
            depth += aim * amount
        else:
            aim += {'down': 1, 'up': -1}[instruction] * amount
    print(depth * hor)
