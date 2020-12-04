import re
def readFromFile(file):
    input = []
    with open(file) as in_file:
        for line in in_file:
            input.append(line)
    input.append("\n")
    return input

def day4part1():
    count = 0
    input = readFromFile("day04.txt")
    passport = ""
    pattern = re.compile(".*(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*")
    for i in input:
        if i == "\n":
            if re.match(pattern, passport.replace("\n", "")):
                count += 1
            passport = ""
        passport += i
    print(count)

def day4part2():
    count = 0
    d = {}
    # 1 split by (\r?\\n){2}
    with open("day04.txt") as in_file:
        for line in in_file:
            if line == "\n":
                count += check_valid(d)
                d = {}
                continue
            for value in line.replace("\n","").split(" "):
                d[value.split(":")[0]] = value.split(":")[1]

    print(count)


def check_valid(d):
    if re.match(".*(?=.*byr)(?=.*iyr)(?=.*eyr)(?=.*hgt)(?=.*hcl)(?=.*ecl)(?=.*pid).*", " ".join(d.keys())):
        if 1920 <= int(d["byr"]) <= 2002 and 2010 <= int(d["iyr"]) <= 2020 and 2020 <= int(d["eyr"]) <= 2030:
            h = d["hgt"]
            if (len(h) == 5 and h.endswith("cm") and 150 <= int(h[0: 3]) <= 193) or (
                    len(h) == 4 and h.endswith("in") and 59 <= int(h[0: 2]) <= 76):
                if re.fullmatch("#[0-9a-f]{6}", d["hcl"]):
                    if re.fullmatch("(amb|blu|brn|gry|grn|hzl|oth)", d["ecl"]):
                        if re.fullmatch("[0-9]{9}", d["pid"]):
                            return 1
    return 0


day4part2()