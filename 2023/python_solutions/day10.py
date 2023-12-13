from queue import Queue
from more_itertools import first_true

DIRS = UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
PIPES = {
    '|': [UP, DOWN],   '-': [LEFT, RIGHT],
    'L': [UP, RIGHT],  'J': [UP, LEFT],
    '7': [LEFT, DOWN], 'F': [RIGHT, DOWN],
}


def add_tuples(t1, t2): return t1[0] + t2[0], t1[1] + t2[1]


class Map(list):
    def __getitem__(self, item):
        if isinstance(item, tuple):
            return super().__getitem__(item[0]).__getitem__(item[1])
        return super().__getitem__(item)

    def in_range(self, item: (int, int)):
        return item[0] in range(self.__len__()) and item[1] in range(self.__getitem__(0).__len__())


def get_path(_map, pos, path):
    while True:
        for _dir in PIPES.get(_map[pos], DIRS):
            new_pos = add_tuples(pos, _dir)
            if (-_dir[0], -_dir[1]) in PIPES.get(_map[new_pos], []) and new_pos not in path:
                path.add(pos := new_pos)
                break
        else:
            return path


def find_outside_spaces(_map, outside_spaces):
    q = Queue()
    q.put((0, 0))
    while not q.empty():
        pos = q.get()
        for _dir in DIRS:
            new_pos = add_tuples(pos, _dir)
            if _map.in_range(new_pos) and new_pos not in outside_spaces and _map[new_pos] != 'S':
                q.put(new_pos)
                outside_spaces.add(new_pos)


def part2(_map: Map):
    new_map = Map()
    for line in _map:
        new_map.extend(''.join(dct[x] for x in line) for dct in [
            {'-': '...', '|': '.|.', 'J': '.|.', 'F': '...', '7': '...', 'L': '.|.', '.': '...', 'S': '.S.'},
            {'-': '---', '|': '.|.', 'J': '-J.', 'F': '.F-', '7': '-7.', 'L': '.L-', '.': '...', 'S': 'SSS'},
            {'-': '...', '|': '.|.', 'J': '...', 'F': '.|.', '7': '.|.', 'L': '...', '.': '...', 'S': '.S.'}
        ])
    s_middle = next((i, row.index('S') + 1) for i, row in enumerate(new_map) if 'SSS' in row)
    path = first_true(get_path(new_map, add_tuples(s_middle, _dir), set()) for _dir in DIRS)
    find_outside_spaces(new_map, path)
    return sum(
        all((rr, cc) not in path for rr in range(r - 1, r + 2) for cc in range(c - 1, c + 2))
        for r in range(len(new_map))
        for c in range(len(new_map[r]))
    ) // 9


def part1(_map: Map):
    start_pos = next((i, row.index('S')) for i, row in enumerate(_map) if 'S' in row)
    return len(get_path(_map, start_pos, {start_pos})) // 2


with open('../inputs/day10.txt') as file:
    _map = Map(file.read().split('\n'))
    print(part1(_map), part2(_map))
