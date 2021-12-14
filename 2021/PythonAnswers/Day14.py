from collections import Counter


def part1(rules, cur, amount):
    ans = []
    for c1, c2 in zip(cur, cur[1:]):
        ans.extend(list(rules[c1 + c2]))
    ans.append(cur[-1])
    return Counter(ans).values() if amount == 1 else part1(rules, ans, amount - 1)


def part2(rules, cur, cache, amount):
    if val := cache.get((cur, amount), False):
        return val
    ans = Counter()
    for c1, c2 in zip(cur, cur[1:]):
        if amount == 1:
            for i in rules[c1 + c2]:
                ans[i] += 1
        else:
            ans += part2(rules, rules[c1 + c2] + c2, cache, amount-1)
    cache[(cur, amount)] = ans
    return ans


if __name__ == '__main__':
    with open("day14") as input_file:
        start_pos, rules_ = input_file.read().split('\n\n')
    rules_ = {fr: fr[0] + to for fr, to in [line.split(' -> ') for line in rules_.split('\n')]}

    ans1 = part1(rules_, start_pos, 10)
    print("part1:", max(ans1) - min(ans1))

    ans2 = (part2(rules_, start_pos, {}, 40) + Counter(start_pos[-1])).values()
    print("part2:", max(ans2) - min(ans2))
