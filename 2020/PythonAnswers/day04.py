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


# this one is longer but more readable
def day4part2option1():
    count = 0
    dic = {}
    with open("day04.txt") as in_file:
        for line in in_file:
            if line == "\n":
                count += check_valid(dic)
                dic = {}
                continue
            for value in line.replace("\n", "").split(" "):
                dic[value.split(":")[0]] = value.split(":")[1]

    print(count)


# this one is shorter but harder to understand
def day4part2option2():
    count = 0
    st = ""
    with open("day04.txt") as in_file:
        for line in in_file:
            if line == "\n":
                if check_valid2(st):
                    count += 1
                st = ""
                continue
            st += line.replace("\n", "")
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


def check_valid2(d):
    return re.match(".*(?=.*(byr:200[0-2]|byr:19[2-9][0-9]))(?=.*(iyr:201[0-9]|iyr:2020))(?=.*(eyr:202[0-9]|eyr:2030))(?=.*(hgt:1[5-8][0-9]cm|hgt:19[0-3]cm|hgt:6[0-9]in|hgt:59in|hgt:7[0-6]in))(?=.*hcl:#[0-9a-f]{6})(?=.*ecl:(amb|blu|brn|gry|grn|hzl|oth))(?=.*pid:[0-9]{9}[a-zA-Z\s]).*", d+" ")


day4part2option1()
day4part2option2()
