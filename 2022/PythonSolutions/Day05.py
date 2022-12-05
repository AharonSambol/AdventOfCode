import re

part1 = True
with open("../Inputs/InputDay05.txt") as file:
    start, moves = file.read().split('\n\n')
    stacks = [[] for _ in range(int(start.split()[-1]))]
    for line in start.split('\n'):
        for i in range(0, len(line), 4):
            if line[i] == '[':
                stacks[i // 4].insert(0, line[i + 1])

    for line in moves.split('\n'):
        amount, frm, to = map(int, re.findall(r'\d+', line))
        to_add = stacks[frm - 1][-amount:][::-1] if part1 else stacks[frm - 1][-amount:]
        stacks[to - 1].extend(to_add)
        stacks[frm - 1] = stacks[frm - 1][:-amount]
    print(''.join(x[-1] for x in stacks))
