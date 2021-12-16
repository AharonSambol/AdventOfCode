def day10(ipt):
    part1_ans, part2_ans = 0, []
    values = {')': (3, 1), ']': (57, 2), '}': (1197, 3), '>': (25137, 4)}
    opposites = {'(': ')', '[': ']', '{': '}', '<': '>'}
    for line in ipt:
        stack = []
        for char in line:
            if char in values:
                if opposites[stack[-1]] == char:
                    stack.pop(-1)
                else:
                    part1_ans += values[char][0]
                    break
            else:
                stack.append(char)
        else:
            part2_ans.append(0)
            for char in stack[::-1]:
                part2_ans[-1] = part2_ans[-1] * 5 + values[opposites[char]][1]
    print(f"part1: { part1_ans }")
    print(f"part2: { sorted(part2_ans)[len(part2_ans) // 2] }")


if __name__ == '__main__':
    with open("day10") as input_file:
        day10([x.strip() for x in input_file.readlines()])
