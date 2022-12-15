import multiprocessing
import re


def part1(sensors, beacons, y, min_x, max_x):
    ranges = [(s_x - w, s_x + w) for s_x, s_y, r in sensors if (w := r - abs(s_y - y)) > 0]
    ranges = [(max(s, min_x), min(e, max_x)) for s, e in ranges if e > min_x and s < max_x]
    res, new_ranges, skip = 0, [], set()
    for i, (r1_start, r1_end) in enumerate(ranges):
        while True:
            for j, (r2_start, r2_end) in enumerate(ranges[i + 1:], start=i+1):
                # if the ranges overlap
                if r1_start <= r2_start <= r1_end or r2_start <= r1_end <= r2_end or \
                        r1_start <= r2_end <= r1_end or r2_start <= r1_start <= r2_end:
                    r1_start, r1_end = min(r1_start, r2_start), max(r1_end, r2_end)
                    ranges.pop(j)
                    break
            else:
                break
        res += r1_end - r1_start + 1
    return res - sum(b[1] == y for b in beacons)

def part2(sensors, y, min_x, max_x):
    ranges = [(s_x - w, s_x + w)
              for s_x, s_y, r in sensors
              if (w := r - abs(s_y - y)) > 0 and s_x - w <= max_x]
    ranges.sort(key=lambda x: x[0])
    mx = min_x
    for r1_start, r1_end in ranges:
        if r1_start <= mx:
            mx = max(r1_end, mx)
        else:
            queue.put(r1_start * 4000000 + y)
            return

def part2_range(sensors, start_y, end_y, min_x, max_x):
    for y in range(start_y, end_y):
        part2(sensors, y, min_x, max_x)

def main():
    with open("../Inputs/InputDay15.txt") as file:
        beacons = set()
        sensors = []
        for line in file:
            s_x, s_y, b_x, b_y = map(int, re.findall(r'-?\d+', line))
            beacons.add((b_x, b_y))
            dist = abs(s_x - b_x) + abs(s_y - b_y)
            sensors.append((s_x, s_y, dist))

        print("part1:", part1(sensors, beacons, 2000000, float("-inf"), float("inf")))
        with multiprocessing.Pool() as pool:
            [pool.apply_async(part2_range, (sensors, start_y, end_y, 0, 4000000))
               for start_y, end_y in
               [(40000 * x, 40000 * (x + 1) + 1) for x in range(100)]]
            print("part2:", queue.get())
            exit()


queue = multiprocessing.Queue()
main()