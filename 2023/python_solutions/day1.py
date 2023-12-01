import re


def part1():
    with open("../inputs/day01.txt") as file:
        print(sum(int(x + y) for x, y in re.findall(r'.*?(?=(\d)).*(\d).*?', file.read())))


def part2():
    numbers = {
        'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5',
        'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
    }
    numbers_re = rf'(\d|{"|".join(numbers.keys())})'
    with open("../inputs/day01.txt") as file:
        print(sum(
            int(numbers.get(x, x) + numbers.get(y, y))
            for x, y in re.findall(rf'.*?(?={numbers_re}).*{numbers_re}.*?', file.read())
        ))


part1()
part2()
