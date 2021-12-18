import re


def part1(hw):
    first_line = hw[0]
    for line in hw[1:]:
        first_line = add(first_line, line)
    return magnitude(first_line)


def part2(hw):
    mx = 0
    for i in range(len(hw)):
        for j in range(len(hw)):
            if i != j:
                mx = max(mx, magnitude(add(hw[i], hw[j])))
    return mx


def magnitude(line):
    new_line, to_pass = [], 0
    while len(line) > 1:
        for i in range(len(line)):
            if to_pass:
                to_pass -= 1
            elif line[i] in ['[', ']']:
                new_line.append(line[i])
            else:
                if type(line[i+1]) is int:
                    new_line[-1] = line[i] * 3 + line[i+1] * 2
                    to_pass = 2
                else:
                    new_line.append(line[i])
        line, new_line = new_line, []
    return line[0]


def add(line1, line2):
    line = ['['] + line1 + line2 + [']']
    while True:
        amount_of_indent, big_chr = 0, -1
        for index, char in enumerate(line):
            if char in ['[', ']']:
                amount_of_indent += {'[': 1, ']': -1}[char]
            elif amount_of_indent > 4:
                left, right = char, line[index+1]
                line[index-1:index+3] = [0]
                for i in range(index-2, -1, -1):
                    if type(line[i]) is int:
                        line[i] = line[i] + left
                        break
                for i in range(index, len(line)):
                    if type(line[i]) is int:
                        line[i] = line[i] + right
                        break
                break
            elif big_chr == -1 and type(char) is int and char >= 10:
                big_chr = index
        else:
            if big_chr == -1:
                break
            val = line.pop(big_chr)
            line[big_chr:big_chr] = ['[', val // 2, val // 2 + val % 2, ']']
    return line


if __name__ == '__main__':
    with open("day18") as input_file:
        ipt = [list(re.findall(r"(\[|]|\d+)", line.strip())) for line in input_file.readlines()]
    ipt = [[int(x) if x.isnumeric() else x for x in line] for line in ipt]
    print(part1(ipt))
    print(part2(ipt))
