nums = {"abcefg": '0', "cf": '1', "acdeg": '2', "acdfg": '3', "bcdf": '4', "abdfg": '5', "abdefg": '6',
        "acf": '7', "abcdefg": '8', "abcdfg": '9'}


def part1():
    return sum(len(x) in [2, 4, 3, 7] for line in ipt for x in line[1])


def get_num(keys, num):
    return ''.join(sorted([keys[x] for x in num]))


# NOTE - this solution was my initial solution before I correctly read the instructions
if cant_read_instructions := True:
    def part2_make_dict(line):
        d = {letter: {'a', 'b', 'c', 'd', 'e', 'f', 'g'} for letter in "abcdefg"}
        for val in line[0] + line[1]:
            for nt in {2: "abdeg", 3: "bdeg", 4: "aeg"}.get(len(val), ''):
                for letter in val:
                    d[letter].discard(nt)
        return d

    def check(keys, line):
        return all(get_num(keys, num) in nums for num in line)

    def brute_force(key, so_far, taken, line, possible):
        if key == 'h':
            return so_far if check(so_far, line) else None
        for val in possible[key]:
            if val in taken:
                continue
            so_far[key] = val
            taken.add(val)
            if ans := brute_force(chr(ord(key) + 1), so_far, taken, line, possible):
                return ans
            taken.remove(val)
        return None

    def part2():
        ans = 0
        for line in ipt:
            keys = brute_force('a', {}, set(), line[0] + line[1], part2_make_dict(line))
            ans += int(''.join(str(nums[get_num(keys, num)]) for num in line[1]))
        return ans
    
else:   # NOTE - this solution is what I came up with *after* correctly reading the instructions
    def smarter_solution():
        with open("day8") as input_text:
            ans = 0
            for line in input_text.readlines():
                ipt, to_solve = line.strip().split(" | ")
                ipt_split = sorted(ipt.strip().split(' '), key=lambda x: len(x))
                key_map = {'a': ipt_split[1]}
                for d in ipt_split[0]:
                    key_map['a'] = key_map['a'].replace(d, "")
                for n in "abcdefg":
                    if (cnt := ipt.count(n)) in [4, 6, 9]:
                        key_map[{4: 'e', 6: 'b', 9: 'f'}[cnt]] = n
                    elif cnt == 8 and n != key_map['a']:
                        key_map['c'] = n
                key_map['d'] = next(n for n in ipt_split[2] if n not in [key_map['b'], key_map['c'], key_map['f']])
                key_map['g'] = next(n for n in ipt_split[9] if n not in key_map.values())
                decrypted_num = ""
                key_map = {v: k for k, v in key_map.items()}
                for num in to_solve.split(' '):
                    decrypted_num += nums[get_num(key_map, num)]
                ans += int(decrypted_num)
            return ans


if __name__ == '__main__':
    print(smarter_solution())
    with open("day8") as input_file:
        ipt = [[v.split(' ') for v in x.strip().split(' | ')] for x in input_file.readlines()]
        print(part1())
        print(part2())
