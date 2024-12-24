def solve(numbers: list[int]) -> tuple[int, int]:
    part1_res = 0
    monkeys = {}
    for number in numbers:
        monkey = {}
        changes = []
        prev_sell = None
        for _ in range(2000):
            number = ((number * 64) ^ number) % 16777216
            number = ((number // 32) ^ number) % 16777216
            number = ((number * 2048) ^ number) % 16777216
            sell_number = number % 10
            if prev_sell is not None:
                changes.append(sell_number - prev_sell)
                if len(changes) > 4:
                    changes.pop(0)
                if len(changes) == 4:
                    tuple_changes = tuple(changes)
                    monkey[tuple_changes] = monkey.get(tuple_changes, sell_number)
            prev_sell = sell_number
        part1_res += number
        for k, v in monkey.items():
            monkeys[k] = monkeys.get(k, 0) + v
    return part1_res, max(monkeys.values())


def main():
    with open('inputs/day22.txt') as f:
        numbers = [int(x) for x in f.read().split('\n')]
    print(solve(numbers))


if __name__ == '__main__':
    main()
