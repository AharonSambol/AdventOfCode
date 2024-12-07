from collections import defaultdict

Rules = dict[str, set[str]]
Update = list[str]


def is_valid(rules: Rules, update: Update) -> bool:
    prev_nums = set()
    for num in update:
        if rules[num] & prev_nums:
            return False
        prev_nums.add(num)
    return True


def part1(rules: Rules, updates: list[Update]) -> int:
    return sum(
        int(update[len(update) // 2])
        for update in updates
        if is_valid(rules, update)
    )


def remove_last(rules: Rules, update: Update) -> str:
    idx, last = next((i, page) for i, page in enumerate(update) if not rules[page] & set(update))
    update.pop(idx)
    return last


def part2(rules: Rules, updates: list[Update]) -> int:
    res = 0
    for update in updates:
        if not is_valid(rules, update):
            for _ in range(len(update) // 2 + 1):
                last = remove_last(rules, update)
            res += int(last)
    return res


def parse_rules(rules: list[str]) -> Rules:
    parsed_rules = defaultdict(set)
    for rule in rules:
        first, second = rule.split('|')
        parsed_rules[first].add(second)
    return parsed_rules


def main():
    with open('inputs/day05.txt') as f:
        rules, updates = [part.split('\n') for part in f.read().split('\n\n')]
        rules = parse_rules(rules)
        updates = [update.split(",") for update in updates]
        print(part1(rules, updates))
        print(part2(rules, updates))


if __name__ == '__main__':
    main()