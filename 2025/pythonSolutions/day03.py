for part1 in [True, False]:
    print(sum((lambda line: sum(x * 10 ** i for i, x in enumerate(reversed([(lambda i: (lambda mi, m: ([line.pop(0) for _ in range(mi + 1)] is None) or m)(*max(enumerate(line[:len(line) - i]), key=lambda x: x[1])))(i) for i in range(1 if part1 else 11, -1, -1)]))))([int(x) for x in line.strip()]) for line in open("inputs/day03.txt")))


# --- CLEAN SOLUTION ---
for part1 in [True, False]:
    with open("inputs/day03.txt") as f:
        res = 0
        for line in f:
            line = [int(x) for x in line.strip()]
            voltage = 0
            for i in range(1 if part1 else 11, -1, -1):
                max_index, max_num = max(enumerate(line[:len(line) - i]), key=lambda x: x[1])
                line = line[max_index + 1:]
                voltage = voltage * 10 + max_num
            res += voltage
        print(res)
