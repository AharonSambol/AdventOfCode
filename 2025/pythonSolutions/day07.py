from collections import defaultdict

with open("inputs/day07.txt") as f:
    start_line, *lines = f.read().split("\n")
    posses = {start_line.index("S"): 1}
    splitters_hit = 0
    for line in lines:
        new_posses = defaultdict(int)
        for pos, timelines in posses.items():
            if line[pos] == '.':
                new_posses[pos] += timelines
            else:
                splitters_hit += 1
                for p in [pos - 1, pos + 1]:
                    if p in range(len(line)):
                        new_posses[p] += timelines
        posses = new_posses
    print("part1:", splitters_hit)
    print("part2:", sum(posses.values()))
