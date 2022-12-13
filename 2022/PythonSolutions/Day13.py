import re
from functools import cmp_to_key


def parse(st):
    path = [res := []]
    for c in re.findall(r'(\d+|\[|])', st[1:-1]):
        match c:
            case '[':
                path[-1].append([])
                path.append(path[-1][-1])
            case ']':   path.pop()
            case _:     path[-1].append(int(c))
    return res


def compare(v1, v2):
    if type(v1) == type(v2) == int:
        return 0 if v1 == v2 else 1 if v1 < v2 else -1
    v1, v2 = map(lambda x: [x] if isinstance(x, int) else x, [v1, v2])
    for first, second in zip(v1, v2):
        if res := compare(first, second):
            return res
    return 0 if len(v1) == len(v2) else 1 if len(v1) < len(v2) else -1

with open("../Inputs/InputDay13.txt") as file:
    ipt = file.read()
    print(sum(i
              for i, lines in enumerate(ipt.split('\n\n'), start=1)
              if compare(*map(parse, lines.split('\n'))) == 1))

    packets = [[[2]], [[6]]] + [parse(line) for line in re.split(r'\n+', ipt)]
    packets.sort(key=cmp_to_key(compare), reverse=True)
    print((packets.index([[2]]) + 1) * (packets.index([[6]]) + 1))
