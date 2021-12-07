from collections import Counter


def day7fast(is_part1):     # optimized solution
    input_ships = dict(Counter(input_data)).items()     # group together identical ships
    # distance -> abs(ship - ps)
    # amount is the amount of identical ships
    calc_cost_part1 = lambda ships, ps: sum(abs(ship - ps) * amount for ship, amount in ships)
    # sum of range eg(01,02,03,04,05) -> amount_of_elements * (first_element + last_element) // 02
    # all that is timed by the amount of identical ships
    calc_cost_part2 = lambda ships, ps: sum(((ab := abs(ship - ps)) * (1 + ab) // 2) * amount for ship, amount in ships)
    calc_cost = calc_cost_part1 if is_part1 else calc_cost_part2
    mn, mx = min(input_data), max(input_data)
    while True:     # binary search
        pos = (mx + mn) // 2
        pos_cost = calc_cost(input_ships, pos)
        if calc_cost(input_ships, pos - 1) < pos_cost:
            mx = pos
        elif calc_cost(input_ships, pos + 1) < pos_cost:
            mn = pos
        else:
            return pos_cost


def day7part1():    # initial slow solution
    return min(sum(abs(ship - dst) for ship in input_data) for dst in range(min(input_data), max(input_data)))


def day7part2():    # initial slow solution
    calc_cost = lambda ships, ps: sum((ab := abs(ship - ps)) * (1 + ab) // 2 for ship in ships)
    return min(calc_cost(input_data, dst) for dst in range(min(input_data), max(input_data)))


with open("day7") as input_file:
    input_data = list(map(int, input_file.read().split(',')))
    print(day7part1())
    print(day7fast(True))
    print(day7part2())
    print(day7fast(False))
