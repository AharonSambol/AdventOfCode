import math
import re


def geodes(prices, cur_robots, resources, time, geodes_so_far, max_robots, cache):
    if all(cur_robots.get(elem, 0) >= amount for elem, amount in prices['geode'].items()):
        return sum(range(time - 1)) \
            + (time - 1 if all(resources[elem] >= amount for elem, amount in prices['geode'].items()) else 0)

    formatted = ','.join(str(cur_robots.get(elem, 0)) for elem in ['ore', 'clay', 'obsidian', 'geode'])
    if formatted in cache:
        for t, rcs, g in cache[formatted]:
            if g >= geodes_so_far and t >= time and all(
                    rcs.get(mat, 0) >= min(
                        resources.get(mat, 0),
                        (time - 1) * (max_robots[mat] - cur_robots.get(mat, 0))
                    ) for mat in ['ore', 'clay', 'obsidian', 'geode']
            ):
                return -1
    cache[formatted] = cache.get(formatted, []) + [(time, resources, geodes_so_far)]

    mx = 0
    for robot, price in prices.items():
        if max_robots[robot] < cur_robots.get(robot, 0) + 1:
            continue
        if all(p in cur_robots for p in price):
            new_time = time - max(
                math.ceil(max(0, amount - resources.get(element, 0)) / cur_robots[element])
                for element, amount in price.items()
            ) - 1
            if new_time == 1 and robot != 'geode' or new_time <= 0:
                continue

            new_resources = resources.copy()
            for r, amount in price.items():
                new_resources[r] = new_resources.get(r, 0) - amount
            for r, amount in cur_robots.items():
                new_resources[r] = new_resources.get(r, 0) + (time - new_time) * amount

            cur_robots[robot] = cur_robots.get(robot, 0) + 1
            res = new_time if robot == 'geode' else 0
            res += geodes(prices, cur_robots, new_resources, new_time, geodes_so_far + res, max_robots, cache)
            cur_robots[robot] -= 1
            if cur_robots[robot] == 0:
                del cur_robots[robot]
            mx = max(mx, res)
    return mx


def parse(line):
    prices, max_robots = {}, {'geode': float('inf')}
    for robot in line.split('. '):
        name = re.search(r'Each (\w+) robot', robot)
        prices[name.group(1)] = costs = {v: int(d) for d, v in re.findall(r'(\d+) (\w+)', robot)}
        for r, amount in costs.items():
            max_robots[r] = max(max_robots.get(r, 0), amount)
    return prices, max_robots


def main():
    with open("../Inputs/InputDay19.txt") as file:
        res1, res2 = 0, 1
        for i, (prices, max_robots) in enumerate(map(parse, file), start=1):
            res1 += i * geodes(prices, {'ore': 1}, {}, 24, 0, max_robots, {})
            res2 *= geodes(prices, {'ore': 1}, {}, 32, 0, max_robots, {}) if i < 4 else 1
        print('part1:', res1)
        print('part2:', res2)


if __name__ == '__main__':
    main()
