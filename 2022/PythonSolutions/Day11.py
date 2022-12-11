import re
from dataclasses import dataclass
from math import prod
from typing import List, Callable


@dataclass
class Monkey:
    items: List[int]
    op: Callable[[int], int]
    test: int
    t: int; f: int
    business: int = 0

part1 = False
with open("../Inputs/InputDay11.txt") as file:
    monkeys = [Monkey(
             [int(x) for x in re.findall(r'\d+', monk[1])],
             eval(f'lambda old: ({ monk[2].split("=")[1] })' + '//3' * part1),
             int(monk[3].removeprefix('Test: divisible by ')),
             int(monk[4].split()[-1]),
             int(monk[5].split()[-1])
        ) for monk in [re.split(r'\n\s*', x) for x in file.read().split('\n\n')]]
    b = prod(x.test for x in monkeys)
    for _ in range(20 if part1 else 10000):
        for i, monk in enumerate(monkeys):
            monk.business += len(monk.items)
            for item in map(monk.op, monk.items):
                monkeys[monk.f if item % monk.test else monk.t].items.append(item % b)
            monk.items.clear()
    print(prod(sorted(monk.business for monk in monkeys)[-2:]))

