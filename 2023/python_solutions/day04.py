import re


with open("../inputs/day04.txt") as file:
    starting_cards = file.readlines()

cards = {i: 1 for i in range(len(starting_cards))}
res = 0
for card_num, line in enumerate(starting_cards):
    winning_numbers = len(re.findall(r'\b(\d+)\b(?=.*\|.*\b\1\b)(?!:)', line))
    res += winning_numbers and 2 ** (winning_numbers - 1)
    for i in range(winning_numbers):
        cards[card_num + 1 + i] += cards[card_num]
print(res, sum(cards.values()))
