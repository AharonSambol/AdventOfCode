import math
import operator
import re
from functools import reduce


def amount_of_solutions(time, best):
    sqrt = math.sqrt(time ** 2 - 4 * best)
    sol1, sol2 = (time + sqrt) / 2, (time - sqrt) / 2
    sol1 = math.floor(sol1) if int(sol1) != sol1 else sol1 - 1
    sol2 = math.ceil(sol2) if int(sol2) != sol2 else sol2 + 1
    return sol1 - sol2 + 1


with open('../inputs/day06.txt') as file:
    times, distances = (re.findall(r'\d+', line) for line in file.readlines())
    print(reduce(operator.mul, (amount_of_solutions(int(time), int(best)) for time, best in zip(times, distances))))
    print(amount_of_solutions(int(''.join(times)), int(''.join(distances))))
