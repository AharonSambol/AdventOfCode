import math


def to_bin(st):
    d = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
         '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
    return list(''.join(d[x] for x in st))


def decode_packet(packet):
    global total
    version, type_id = (int(''.join(x), 2) for x in [packet[:3], packet[3:6]])
    [packet.pop(0) for _ in range(6)]
    total += version
    if type_id == 4:  # literal value
        final_str, is_last = "", False
        while not is_last:
            is_last = packet.pop(0) == '0'
            final_str += ''.join([packet.pop(0) for _ in range(4)])
        return int(final_str, 2)
    if packet.pop(0) == '0':
        sub_ln = int(''.join([packet.pop(0) for _ in range(15)]), 2)
        part = packet[:sub_ln]
        [packet.pop(0) for _ in range(sub_ln)]
        results = []
        while len(part) > 0:
            results.append(decode_packet(part))
    else:
        sub_amount = int(''.join([packet.pop(0) for _ in range(11)]), 2)
        results = [decode_packet(packet) for _ in range(sub_amount)]
    return [sum, math.prod, min, max, None, lambda a: 1 if a[0] > a[1] else 0, lambda a: 1 if a[0] < a[1] else 0,
            lambda a: 1 if a[0] == a[1] else 0][type_id](results)


if __name__ == '__main__':
    total = 0
    with open("day16") as input_file:
        part2 = decode_packet(to_bin(input_file.read()))
    print(f"part1: {total}\npart2: {part2}")
