import re

with open("../Inputs/InputDay04.txt") as file:
    res1 = res2 = 0
    for line in file:
        start1, end1, start2, end2 = map(int, re.split(r'[,-]', line))

        res1 += start1 <= start2 <= end2 <= end1 or start2 <= start1 <= end1 <= end2
        res2 += start1 <= start2 <= end1 or start2 <= start1 <= end2
    print(res1, res2)
