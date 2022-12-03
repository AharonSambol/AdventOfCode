from string import ascii_letters as alphabet

part1 = True
with open("../Inputs/InputDay03.txt") as file:
    res = 0
    if part1:
        for line in file:
            half = len(line) // 2
            same = (set(line[:half]) & set(line[half:])).pop()
            res += alphabet.index(same) + 1
    else:
        file = file.read().split('\n')
        for a, b, c in zip(file[::3], file[1::3], file[2::3]):
            same = (set(a) & set(b) & set(c)).pop()
            res += alphabet.index(same) + 1
    print(res)
