with open("day1") as input_file:
    lines = list(map(int, input_file.readlines()))
    # part 1
    print(sum(1 for prev, num in zip(lines, lines[1:]) if num > prev))

    # part 2
    ans, prev = 0, sum(lines[:3])
    for num1, num2, num3 in zip(lines, lines[1:], lines[2:]):
        ans += 1 if (sm := num1 + num2 + num3) > prev else 0
        prev = sm
    print(ans)
