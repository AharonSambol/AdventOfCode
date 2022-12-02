# Not meant to be readable, just as short as possible
with open("../Inputs/InputDay02.txt") as file:
    res1 = res2 = 0
    for line in file.readlines():
        o, me = ord(line[0]) - 64, ord(line[2]) - 87
        res1 += me + \
            3 * (me == o) + \
            6 * (me - 1 == o % 3)
        res2 += 1 + \
            (me == 1) * (o + 1) % 3 + \
            (me == 2) * (o + 2) + \
            (me == 3) * (o % 3 + 6)
    print(res1, res2)
