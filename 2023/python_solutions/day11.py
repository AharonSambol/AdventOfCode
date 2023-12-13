import itertools

for increase in [1, 999_999]:
    with open('../inputs/day11.txt') as file:
        lines = file.read().split('\n')
        empty_lines = [i for i, line in enumerate(lines) if '#' not in line]
        empty_cols = [i for i in range(len(lines[0])) if all(line[i] == '.' for line in lines)]
        galaxies = [
            (r + sum(increase for i in empty_lines if i < r), c + sum(increase for i in empty_cols if i < c))
            for r, line in enumerate(lines)
            for c, item in enumerate(line)
            if item == '#'
        ]
        print(sum(b[0] - a[0] + abs(a[1] - b[1]) for a, b in itertools.combinations(galaxies, 2)))
