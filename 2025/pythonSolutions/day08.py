import math


with open("inputs/day08.txt") as f:
    all_points = [tuple([int(x) for x in line.split(",")]) for line in f.read().split("\n")]
    distances = []
    for i, point in enumerate(all_points): # todo functools.combinations
        for i2, point2 in enumerate(all_points[i + 1:]):
            distances.append(((point, point2), math.sqrt(sum(abs(x1-x2) ** 2 for x1, x2 in zip(point, point2)))))
    distances.sort(key=lambda x: x[1])

    groups = [{point} for point in all_points]
    connection_count = 0
    for points, distance in distances:
        groups_to_join = [
            next(i for i, group in enumerate(groups) if point in group)
            for point in points
        ]
        if groups_to_join[0] != groups_to_join[1]:
            if len(groups) == 2:
                print("part2:", points[0][0] * points[1][0])
            groups[min(groups_to_join)] |= groups.pop(max(groups_to_join))
        connection_count += 1
        if connection_count == 1000:
            largest = [len(group) for group in groups[:3]]
            largest.sort(reverse=True)
            for group in groups[3:]:
                if len(group) > largest[-1]:
                    largest = sorted([*largest, len(group)], reverse=True)[:-1]

            print("part1:", largest[0] * largest[1] * largest[2])
