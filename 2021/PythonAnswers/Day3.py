def most_common(arr, i):
    return '1' if sum(line[i] == '1' for line in arr) >= len(arr) / 2 else '0'


def bin_not(num):
    return ''.join({'1': '0', '0': '1'}[x] for x in num)


with open("day3") as input_file:
    input_data = [x.strip() for x in input_file.readlines()]
    bin_nums_len = len(input_data[0])

    # part 01
    gama = ''.join(most_common(input_data, i) for i in range(bin_nums_len))
    epsilon, gama = int(bin_not(gama), 2), int(gama, 2)
    print(gama * epsilon)

    # part 02
    oxygen = co2 = input_data
    for i in range(bin_nums_len):
        if len(oxygen) > 1:
            common = most_common(oxygen, i)
            oxygen = list(filter(lambda x: x[i] == common, oxygen))
        if len(co2) > 1:
            rare = bin_not(most_common(co2, i))
            co2 = list(filter(lambda x: x[i] == rare, co2))
    oxygen, co2 = int(''.join(oxygen[0]), 2), int(''.join(co2[0]), 2)
    print(oxygen * co2)
