with open("day1") as input_file:
    lines = list(map(int, input_file.readlines()))
    # part 1
    print(sum(1 for prev, num in zip(lines, lines[1:]) if num > prev))

    # part 2
    print(sum(1 for num1, num4 in zip(lines, lines[3:]) if num1 < num4))
