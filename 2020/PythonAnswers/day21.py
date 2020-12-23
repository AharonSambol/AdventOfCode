import re


def read_input_chunks(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day21():
    all_foods = set()
    allergies = set()

    input = list(read_input_chunks("day21.txt"))
    for line in input:
        # <this chunk should be in a function but im lazy :) >
        f = re.split("(?: \\(contains.*| )", line)
        all_foods.update([i.strip() for i in list(filter(lambda x: x != "" and x != "\n", f))])
        a = re.split("(?:.*\\(contains|, |\\))", line)
        allergies.update([i.strip() for i in list(filter(lambda x: x != "" and x != "\n", a))])
        # <\this chunk should be in a function but im lazy :) >
    all_allergies = {}
    for allergy in allergies:
        all_allergies[allergy] = list(all_foods)

    for line in input:
        f = re.split("(?: \\(contains.*| )", line)
        foods = [i.strip() for i in list(filter(lambda x: x != "" and x != "\n", f))]
        a = re.split("(?:.*\\(contains|, |\\))", line)
        allergies = [i.strip() for i in list(filter(lambda x: x != "" and x != "\n", a))]

        # 1 if the alergy is in a line without a certain food it cant be in that food
        # 2 maybe make for each allergy all the foods and for each line its in remove all the foods not in that lne
        for allergy in allergies:
            all_allergies[allergy] = list(filter(lambda food: food in all_allergies[allergy], foods))

    # for each range the only has one option remove that option from all the other ranges
    keep_going = True
    while keep_going:
        keep_going = False
        for allergy in all_allergies:
            if len(all_allergies[allergy]) == 1:
                looking_for = all_allergies[allergy][0]
                for algy2 in all_allergies:
                    if algy2 != allergy and looking_for in all_allergies[algy2]:
                        all_allergies[algy2].remove(looking_for)
            if len(all_allergies[allergy]) > 1:
                keep_going = True
    print(all_allergies)

    count = 0
    all_allergies_lst = [x[0] for x in all_allergies.values()]

    for line in input:
        f = re.split("(?: \\(contains.*| )", line)
        foods = [i.strip() for i in list(filter(lambda x: x != "" and x != "\n", f))]
        for food in foods:
            if food not in all_allergies_lst:
                count += 1
    print("Part One:", count)

    st = ""
    key_order = sorted(all_allergies.keys())
    for key in key_order:
        st += all_allergies[key][0] + ","
    print(st[:-1])


day21()
