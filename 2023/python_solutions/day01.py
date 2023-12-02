import re


def solution(numbers):
    numbers.update({str(x): x for x in range(1, 10)})
    numbers_re = f'({"|".join(numbers.keys())})'
    with open("../inputs/day01.txt") as file:
        print(sum(
            numbers[x] * 10 + numbers[y]
            for x, y in re.findall(f'(?={numbers_re}).*{numbers_re}', file.read())
        ))


solution({})
solution(dict(zip('one two three four five six seven eight nine'.split(), range(1, 10))))
