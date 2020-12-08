import re


def read_input_chunks():
    with open("day07.txt") as in_file:
        for line in in_file:
            yield line


def day7(part_one):
    input = read_input_chunks()
    hm = {}
    for line in input:
        thisBag = line.split(" bags contain")[0]
        if "no other bags" in line:
            hm[thisBag] = []
            continue
        ListOfBags = []
        allBags = re.split("(?:.*contain (\\d) | bags?, (\\d) | bags?\\.\\n?)", line)
        allBags = list(filter(lambda x: x != "" and x is not None, allBags))
        amount = 0
        for i, bag in enumerate(allBags):
            if bag.isnumeric():
                amount = int(bag)
            else:
                for _ in range(amount):
                    ListOfBags.append(bag)
        hm[thisBag] = ListOfBags
    if part_one:
        print(find_all(hm, "shiny gold", 0))
    else:
        print(find_amount(hm, "shiny gold", 0))


def find_all(d, color, count):
    for key in d:
        if color in d[key]:
            d[key] = []
            count = find_all(d, key, count) + 1
    return count


def find_amount(d, color, count):
    for bag in d[color]:
        count = find_amount(d, bag, count) + 1
    return count


day7(True)
