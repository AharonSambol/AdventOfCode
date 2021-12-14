with open("day1") as input_file:
    lines = list(map(int, input_file.readlines()))
    # part 1
    print(sum(num > prev for prev, num in zip(lines, lines[1:])))

    # part 2
    print(sum(num1 < num4 for num1, num4 in zip(lines, lines[3:])))
