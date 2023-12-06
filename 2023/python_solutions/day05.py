import itertools
import re


def map_seeds(start, amount, mapping):
    for dest_start, source_start, rng_len in mapping:
        offset = dest_start - source_start
        smaller = max(0, min(source_start - start, amount))
        bigger = max(0, min((start + amount) - (source_start + rng_len), amount))
        if bigger != amount:
            yield start, smaller    # smaller seeds
            yield start + smaller + offset, amount - bigger - smaller   # in range seeds
            if bigger:
                yield from map_seeds(start + amount - bigger, bigger, mapping)  # bigger seeds
            return


with open("../inputs/day05.txt") as file:
    seeds_line, *chunks = re.split(r'\n\n[\w\- ]+:\n', file.read())

chunks = [
    sorted([
        [int(x) for x in line.split()]
        for line in chunk.split('\n')
    ], key=lambda rng: rng[1])
    for chunk in chunks
]

for part in [True, False]:
    seeds = (int(x) for x in seeds_line.removeprefix('seeds: ').split())
    seeds = [(seed, 1 if part else next(seeds)) for seed in seeds]
    for chunk in chunks:
        seeds = [x for x in itertools.chain(*[map_seeds(*seed, chunk) for seed in seeds]) if x[1]]
    print(min(seeds, key=lambda x: x[0])[0])
