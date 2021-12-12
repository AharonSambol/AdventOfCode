def calc(caves, from_cave, path, visited_twice):
    amount = 0
    if from_cave == 'end':
        return 1
    for dest in caves.get(from_cave, []):
        if dest.islower() and (path.get(dest, 0) == 2 or (path.get(dest, 0) == 1 and visited_twice)):
            continue
        path[from_cave] = path.get(from_cave, 0) + 1
        amount += calc(caves, dest, path, visited_twice or (dest.islower() and path.get(dest, 0) == 1))
        path[from_cave] -= 1
    return amount

if __name__ == '__main__':
    caves = dict()
    with open("input.txt") as input_file:
        for line in input_file.readlines():
            from_cave, to_cave = line.strip().split("-")
            for from_cave, to_cave in [(from_cave, to_cave),  (to_cave, from_cave)]:
                caves[from_cave] = caves.get(from_cave, []) + [to_cave]
        print(calc(caves, 'start', {'start': 1}, False))
