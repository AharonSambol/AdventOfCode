from functools import reduce


print("part1:", reduce(lambda t, n: (t[0] + n, t[1] + ((t[0] + n) % 100 == 0)), (int(line.strip("R ").replace("L", "-")) for line in open("inputs/day01.txt", "r")), (50, 0))[1])
print("part2:", reduce(lambda t, n: ((t[0] + n) % 100, t[1] + ((n // abs(n) * t[0]) % 100 + abs(n)) // 100), (int(line.strip("R ").replace("L", "-")) for line in open("inputs/day01.txt", "r")), (50, 0))[1])


