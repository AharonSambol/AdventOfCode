part1 = False
with open("InputDay1") as file:
    elves = file.read().strip().split('\n\n')
    elves = (sum(map(int, elf.split('\n'))) for elf in elves)
    print(max(elves) if part1 else sum(sorted(elves)[-3:]))
