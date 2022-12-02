part1 = False
with open("../Inputs/InputDay01.txt") as file:
    elves = file.read().split('\n\n')
    elves = (sum(map(int, elf.split('\n'))) for elf in elves)
    print(max(elves) if part1 else sum(sorted(elves)[-3:]))
