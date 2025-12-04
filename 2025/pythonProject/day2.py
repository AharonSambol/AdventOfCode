import re

for part1 in [True, False]:
    print(sum(sum(x for x in range(int(start), int(end) + 1) if re.fullmatch(r"(\d+)\1" + ("" if part1 else "+"), str(x))) for start, end in [r.split("-") for r in open("inputs/day2.txt").read().split(",")]))
