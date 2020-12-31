import copy
import re


def read_input(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day24pt1():
    all_tiles = {}
    input = [re.findall("(e|se|sw|nw|w|ne)", line) for line in read_input("day24.txt")]
    dirs = {"e": (0, 1), "se": (1, 0), "sw": (1, -1), "nw": (-1, 0), "w": (0, -1), "ne": (-1, 1)}
    for line in input:
        row, col = 100, 100
        for dir in line:
            row += dirs[dir][0]
            col += dirs[dir][1]

        pos = str(row)+","+str(col)
        if pos in all_tiles:
            all_tiles.pop(pos)
        else:
            all_tiles[pos] = None

    print("part one:", len(all_tiles))
    return all_tiles


def day24pt2():
    get_around = [(-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1)]
    on_tiles = day24pt1()
    for _ in range(100):
        all_tiles = {}
        for tile in on_tiles.keys():
            for side in get_around:
                r, c = side
                row, col = tile.split(",")
                all_tiles[str(int(row)+r) + "," + str(int(col)+c)] = None

        new_on_tiles = {}
        for tile in all_tiles.keys():
            r, c = tile.split(",")
            nbrs = get_neighbors(on_tiles, int(r), int(c))
            if tile in on_tiles:
                if nbrs != 0 and nbrs <= 2:
                    new_on_tiles[tile] = None
            else:
                if nbrs == 2:
                    new_on_tiles[tile] = None
        on_tiles = copy.deepcopy(new_on_tiles)

    print("part two:", len(on_tiles))


def get_neighbors(tiles, r, c):
    ans = [tiles.get(str(r-1)+","+str(c), 1), tiles.get(str(r-1)+","+str(c+1), 1), tiles.get(str(r)+","+str(c-1), 1),
           tiles.get(str(r)+","+str(c+1), 1), tiles.get(str(r+1)+","+str(c), 1), tiles.get(str(r+1)+","+str(c-1), 1)]
    return len([x for x in ans if x is None])


day24pt2()
