def read_input(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day18():
    input = read_input("day18.txt")
    count = 0
    for line in input:
        count += calc(line)
    print(count)


def calc(line):
    without_brackets = ""
    amountOfOpen = 0
    sub = ""
    start = False
    for char in line:
        if char == "(":
            amountOfOpen += 1
            if start:
                sub += char
            start = True
        elif char == ")":
            amountOfOpen -= 1
            if amountOfOpen == 0:
                without_brackets += str(calc(sub))
                sub = ""
                start = False
            else:
                sub += char
        elif start:
            sub += char
        else:
            without_brackets += char
    # pt 1
    return do_plus_times(without_brackets)
    # pt 2
    return do_times(do_plus(without_brackets))


def do_plus_times(line):
    line = line.split(" ")
    line = list(filter(lambda x: x != "", line))
    first = int(line[0])
    line.pop(0)
    func = ""
    for second in line:
        if second == "+" or second == "*":
            func = second
        else:
            if func == "+":
                print(first, second)
                first = first + int(second)
            else:
                first = first * int(second)
    return first


def do_plus(line):
    line = line.split(" ")
    line = list(filter(lambda x: x != "", line))
    for i in range(len(line)):
        if line[i] == "+":
            line[i+1] = str(int(line[i-1]) + int(line[i+1]))
            line[i - 1] = "+"

    line = list(filter(lambda x: x != "+", line))
    line = " ".join(line)
    return line.strip()


def do_times(line):
    print(line)
    line = line.split(" ")
    line = list(filter(lambda x: x != "" and x != "*", line))
    first = int(line[0])
    line.pop(0)
    for second in line:
        first = first * int(second)
    return first


day18()
