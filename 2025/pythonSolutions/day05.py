with (open("inputs/day05.txt") as f):
    ranges, ingredients = f.read().split("\n\n")
    print("part1:", sum(any(ingredient in range(*map(int, r.split("-"))) for r in ranges.split("\n")) for ingredient in map(int, ingredients.split("\n"))))

    ranges, filtered_ranges = [], [[int(x) for x in rng.split("-")] for rng in ranges.split("\n")]
    while len(ranges) != len(filtered_ranges):
        ranges = filtered_ranges
        filtered_ranges = []
        for cur_range in ranges:
            for i, other_range in enumerate(filtered_ranges):
                if any(
                        x in range(r1[0], r1[1] + 1)
                        for r1, r2 in [(cur_range, other_range), (other_range, cur_range)]
                        for x in r2
                ):
                    filtered_ranges[i] = [min(cur_range[0], other_range[0]), max(cur_range[1], other_range[1])]
                    break
            else:
                filtered_ranges.append(cur_range)
    print("part2:", sum(rng[1] - rng[0] + 1 for rng in filtered_ranges))
