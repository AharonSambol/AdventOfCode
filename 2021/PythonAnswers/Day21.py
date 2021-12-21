def part1(p1, p2):
    die = die_times = 0
    while True:
        for player in [p1, p2]:
            player[0] = (player[0] + (die+1) * 3 + 3) % 10
            die = (die + 3) % 100
            die_times += 3
            player[1] += player[0] + 1
            if player[1] >= 1_000:
                return die_times * (p2[1] if player == p1 else p1[1])

cache = {}
def part2(p1, p2, turn):
    if (*p1, *p2, turn) in cache:
        return cache[(*p1, *p2, turn)]
    p1_wins = p2_wins = 0
    for die in range(3, 9 + 1):
        player = p1 if turn == 1 else p2 
        cpy = [(player[0] + die) % 10, player[1]]
        cpy[1] += cpy[0] + 1
        if cpy[1] >= 21:
            win1, win2 = turn, (1-turn)
        else:
            win1, win2 = part2(cpy if turn else p1, cpy if not turn else p2, 1-turn)
        amount = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}[die]
        p1_wins += win1 * amount
        p2_wins += win2 * amount
    cache[(*p1, *p2, turn)] = (p1_wins, p2_wins)
    cache[(*p2, *p1, 1-turn)] = (p2_wins, p1_wins)  # not sure if helps...
    return p1_wins, p2_wins


print(part1([10 - 1, 0], [2 - 1, 0]))
print(part2([10 - 1, 0], [2 - 1, 0], 1))
