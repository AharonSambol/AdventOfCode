part2 = True
with open("../Inputs/InputDay20.txt") as file:
    lst = [(int(x) * (811589153 if part2 else 1), i) for i, x in enumerate(file)]
    order = tuple(x for x in lst)
    for _ in range(10 if part2 else 1):
        for ct in range(len(lst)):
            i = lst.index(order[ct])
            val = lst.pop(i)
            lst.insert((i + val[0]) % len(lst), val)
    zero = next(i for i, x in enumerate(lst) if x[0] == 0)
    print(sum(lst[(zero + 1000 * x) % len(lst)][0] for x in (1, 2, 3)))
