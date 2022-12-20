part2 = True
class Pointer:
    def __init__(self, pos, orig):
        self.pos = pos
        self.orig = orig

with open("../Inputs/InputDay20.txt") as file:
    lst = [int(i) * (811589153 if part2 else 1) for i in file]
    lst = [Pointer(x if x >= 0 else x % -(len(lst) - 1), x) for x in lst]
    order = [x for x in lst]
    for _ in range(10 if part2 else 1):
        for ct in range(len(lst)):
            i = lst.index(order[ct])
            val = lst.pop(i)
            lst.insert((i + val.pos) % len(lst), val)
    zero = next(i for i, x in enumerate(lst) if x.orig == 0)
    print(sum(lst[(zero + 1000 * x) % len(lst)].orig for x in (1, 2, 3)))
