import re


def read_input_chunks():
    with open("day07.txt") as in_file:
        for line in in_file:
            yield line


def day7(partOne):
    input = read_input_chunks()
    hm = {}
    for line in input:
        thisBag = line.split("s contain")[0]
        if line.__contains__("no other bags"):
            hm[thisBag] = []
            continue
        allBags = []
        for i, bag in enumerate(re.split("(^.*contain|, |\\.)", line)):
            if not re.match(".*(, |\\.|contain|\n|^$).*", bag):
                amount = int(re.findall("\\d", bag)[0])
                for _ in range(amount):
                    allBags.append(bag.strip().replace("bags", "bag")[len(str(amount))+1:])
        hm[thisBag] = allBags
    if partOne:
        print(find_all(hm, "shiny gold bag", 0))
    else:
        print(find_amount(hm, "shiny gold bag", 0))

def find_all(d, color, count):
    for key in d:
        if d[key].__contains__(color):
            d[key] = []
            count = find_all(d, key, count) + 1
    return count


def find_amount(d, color, count):
    for bag in d[color]:
        count = find_amount(d, bag, count) + 1
    return count

day7(False)
