import re
from collections import defaultdict

with open("../Inputs/InputDay07.txt") as file:
    dirs, path = defaultdict(int), []
    commands = re.split(r'\n\$ ', '\n' + file.read())
    for cmd in commands:
        if cmd.startswith('cd'):
            path = path[:-1] if cmd == 'cd ..' else path + [cmd.removeprefix('cd ')]
        else:
            size = sum(int(x.split()[0]) for x in cmd.split('\n')[1:] if not x.startswith('dir'))
            for i in range(len(path)):
                dirs['/'.join(path[:i+1])] += size
    print(sum(x for x in dirs.values() if x <= 100000))
    print(min([x for x in dirs.values() if x >= dirs['/'] - 40000000]))
