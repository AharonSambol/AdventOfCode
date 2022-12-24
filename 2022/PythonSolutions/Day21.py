# has assumption that `humn` is never multiplied by itself
def get_monkey_val(name, monkey, monkeys, part2):
    if monkey.isnumeric():
        return complex(0, 1) if name == 'humn' and part2 else complex(int(monkey), 0)
    m1, op, m2 = monkey.split()
    if name == 'root' and part2:
        m1, m2 = get_monkey_val(m1, monkeys[m1], monkeys, part2), get_monkey_val(m2, monkeys[m2], monkeys, part2)
        return (m1.real - m2.real) // (m2.imag - m1.imag)
    return eval(f'{get_monkey_val(m1, monkeys[m1], monkeys, part2)}{op}{get_monkey_val(m2, monkeys[m2], monkeys, part2)}')

with open("../Inputs/InputDay21.txt") as file:
    monkeys = {name: val for name, val in (line.strip().split(': ') for line in file)}
    for part in range(1, 3):
        print(f'part{part}:', int(get_monkey_val('root', monkeys['root'], monkeys, part == 2).real))
