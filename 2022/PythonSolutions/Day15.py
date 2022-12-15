import multiprocessing
import re


def part1(sensors, beacons, y):
    ranges = [(s_x - w, s_x + w) for s_x, s_y, r in sensors if (w := r - abs(s_y - y)) > 0]
    res = 0
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

def part2(sensors, y, start, end):
    ranges = [(s_x - w, s_x + w) for s_x, s_y, r in sensors
              if (w := r - abs(s_y - y)) > 0 and s_x - w <= end]
    ranges.sort(key=lambda x: x[0])
    for r1_start, r1_end in ranges:
        if r1_start <= start:
            start = max(r1_end, start)
        else:
            queue.put((r1_start - 1) * 4000000 + y)
            return

def part2_range(sensors, start_y, end_y):
    for y in range(start_y, end_y):
        part2(sensors, y, 0, 4000000)

def main():
    with open("../Inputs/InputDay15.txt") as file:
        beacons, sensors = set(), []
        for line in file:
            s_x, s_y, b_x, b_y = map(int, re.findall(r'-?\d+', line))
            beacons.add((b_x, b_y))
            sensors.append((s_x, s_y, abs(s_x - b_x) + abs(s_y - b_y)))

        print("part1:", part1(sensors, beacons, 2000000))
        with multiprocessing.Pool() as pool:
            for i in range(100):
                pool.apply_async(part2_range, (sensors, 40000 * i, 40000 * (i + 1) + 1))
            print("part2:", queue.get())


queue = multiprocessing.Queue()
main()

