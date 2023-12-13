def compare(arr1, arr2, is_part1):
    return len([1 for row1, row2 in zip(arr1, arr2) for a, b in zip(row1, row2) if a != b]) == is_part1


def find_mirror_pos(mp, is_part1):
    return next((i for i, line in enumerate(mp[1:], start=1) if compare(mp[:i][::-1], mp[i:], is_part1)), 0)


with open("../inputs/day13.txt") as file:
    maps = [mp.split('\n') for mp in file.read().split('\n\n')]
for is_part1 in [0, 1]:
    print(sum(find_mirror_pos(mp, is_part1) * 100 or find_mirror_pos(list(zip(*mp[::-1])), is_part1) for mp in maps))
