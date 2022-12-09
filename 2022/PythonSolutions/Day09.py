with open("../Inputs/InputDay09.txt") as file:
    rope = [(0, 0)] * 10
    visited2, visited1 = {(0, 0)}, {(0, 0)}
    for line in file:
        dr = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}[line[0]]
        for _ in range(int(line.split()[1])):
            rope[0] = rope[0][0] + dr[0], rope[0][1] + dr[1]
            for k, knot in enumerate(rope[1:], start=1):
                diff = rope[k-1][0] - knot[0], rope[k-1][1] - knot[1]
                if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                    diff = [x // max(1, abs(x)) for x in diff]
                    rope[k] = knot[0] + diff[0], knot[1] + diff[1]
            visited1.add(rope[1])
            visited2.add(rope[-1])
    print(f'part1: {len(visited1)}, part2: {len(visited2)}')
