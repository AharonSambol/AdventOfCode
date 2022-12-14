part1 = False
with open("../Inputs/InputDay14.txt") as file:
    board, max_y = set(), 0
    for line in file:
        line = [list(map(int, x.split(','))) for x in line.split(' -> ')]
        max_y = max(max_y, max(t[1] for t in line))
        for (x1, y1), (x2, y2) in zip(line, line[1:]):
            for x in range(min(x1, x2), max(x1, x2) + 1):
                for y in range(min(y1, y2), max(y1, y2) + 1):
                    board.add((x, y))
    rocks, path = len(board), []
    sand = (500, 0)
    while not (part1 and sand[1] + 1 > max_y):
        path.append(sand)
        if sand[1] < max_y + 1:
            if (sand := (sand[0], sand[1] + 1)) not in board:
                continue
            if (sand := (sand[0] - 1, sand[1])) not in board:
                continue
            if (sand := (sand[0] + 2, sand[1])) not in board:
                continue
        board.add(path[-1])
        if len(path) == 1:
            break
        sand, path = path[-2], path[:-2]
    print(len(board) - rocks)