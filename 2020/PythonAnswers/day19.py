import re


def read_input(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day19():    #my part 2 sulution is terrible bcs i just modified the input....
    input = read_input("dec19.txt")
    unknown_nums = {}
    known_nums = {}
    for line in input:
        if line == "\n":
            break
        line_num = line.split(":")[0]
        info = line.split(":")[1].strip()
        if "\"" in line:
            known_nums[line_num] = info.replace("\"", "")
        else:
            unknown_nums[line_num] = info

    changed = True
    while changed:
        changed = False
        to_pop = []
        for key in unknown_nums:
            info = unknown_nums[key].split(" ")
            new_info = ""
            is_known = True

            for clue in info:
                if clue == "|":
                    new_info += " |"
                elif clue == "(" or clue == ")*":
                    new_info += " " + clue
                elif "(" in clue:
                    new_info += " " + clue
                elif clue in known_nums:
                    new_info += " (" + known_nums[clue] + ")"
                else:
                    new_info += " " + clue
                    is_known = False
            if is_known:
                to_pop.append(key)
                known_nums[key] = new_info.strip()
            else:
                unknown_nums[key] = new_info.strip()
        for key in to_pop:
            changed = True
            unknown_nums.pop(key)
    count = 0
    for line in input:
        if matches(known_nums, line):
            count += 1
    print(count)


def matches(known_nums, line):
    rgx = known_nums["0"].replace(" ", "")
    if re.fullmatch(rgx, line.strip()) is None:
        return False
    return True


day19()