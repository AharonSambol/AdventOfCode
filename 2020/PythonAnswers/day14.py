import re


def read_input_chunks(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day14pt1(do_pt1):
    m = {}
    input = list(read_input_chunks("day14.txt"))
    for line in input:
        if "mask" in line:
            mask = line.split(" = ")[1]
            continue
        if do_pt1:
            pt1(line, m, mask)
        else:
            pt2(line, m, mask)
    count = 0
    for key in m.keys():
        if do_pt1:
            count += to_decimal(m[key])
        else:
            count += m[key]
    return count


def pt1(line, m, mask):
    pls = re.split("[\\[\\]]", line)[1]
    num = to_binary(line.split(" = ")[1], len(mask))
    m[pls] = apply_mask1(num, mask)


def pt2(line, m, mask):
    places = apply_mask2(to_binary(re.split("[\\[\\]]", line)[1], len(mask)), mask)
    num = int(line.split(" = ")[1])
    for plc in places:
        m[plc] = num


def to_binary(num, st_len):
    return re.split("b", str(bin(int(num))))[1].zfill(st_len)


def apply_mask1(line, mask):
    newLine = ""
    mask = mask.rjust(len(line)+1, "X")
    for char, mChar in zip(line, mask):
        if mChar != "X":
            newLine += mChar
        else:
            newLine += char
    return newLine


def apply_mask2(line, mask):
    list = []
    mask = mask.rjust(len(line) + 1, "0")
    amount_of_x = 0
    template = ""
    for char, mChar in zip(line, mask):
        if mChar != "0":
            if mChar == "X":
                amount_of_x += 1
            template += mChar
        else:
            template += char
    b = bin(0)
    max = bin(int(to_decimal("".rjust(amount_of_x, "1"))))
    while b <= max:
        b_st = re.split("b", b)[1].rjust(amount_of_x, "0")
        indx = 0
        new_product = ""
        for c in template:
            if c == "X":
                new_product += b_st[indx]
                indx += 1
            else:
                new_product += c
        list.append(new_product)
        b = bin(to_decimal(b_st)+1)
    return list


def to_decimal(bi):
    count = 0
    bi = bi[::-1]
    for i, dig in enumerate(bi):
        if dig == "1":
            count += pow(2, i)
    return count


print(day14pt1(True))
print(day14pt1(False))
