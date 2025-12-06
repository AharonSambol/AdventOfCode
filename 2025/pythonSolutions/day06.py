import re
from math import prod

print("part 1:", sum({"+": sum, "*": prod}[operator](map(int, nums)) for *nums, operator in zip(*[re.split(r"\s+", line.strip()) for line in open("inputs/day06.txt").read().split("\n")])))

# --- CLEAN SOLUTION ---
OPERATIONS = {"+": sum, "*": prod}

with open("inputs/day06.txt") as f:
    content = f.read().split("\n")
    lines = [re.split(r"\s+", line.strip()) for line in content]
    res = 0
    for *nums, operator in zip(*lines):
        res += OPERATIONS[operator](map(int, nums))
    print("part 1:", res)

    max_line_len = max(len(x) for x in content)
    *num_lines, op_lines = [line.ljust(max_line_len) for line in content]

    operations = re.split(r"\s(?=[+*])", op_lines)
    start_index = 0
    res = 0
    for operation in operations:
        nums = [
            int(num)
            for i in range(start_index, start_index + len(operation))
            if (num := "".join(line[i] for line in num_lines)).strip()
        ]
        res += OPERATIONS[operation[0]](nums)
        start_index += 1 + len(operation)
    print("part 2:", res)
