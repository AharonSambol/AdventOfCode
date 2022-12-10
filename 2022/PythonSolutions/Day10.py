def tick(cycle, crt, x_pos, r2):
    r2[crt // 40][crt % 40] = '#' if abs(x_pos - crt % 40) < 2 else '.'
    return (cycle % 40 == 20) * cycle * x_pos


with open("../Inputs/InputDay10.txt") as file:
    x, pos, c, res1 = 1, -1, 0, 0
    res2 = [[''] * 40 for _ in range(6)]
    for line in file:
        res1 += tick(c := c + 1, pos := pos + 1, x, res2)
        if line.startswith('add'):
            res1 += tick(c := c + 1, pos := pos + 1, x, res2)
            x += int(line.split()[1])
    print(res1, '\n'.join(''.join(x) for x in res2), sep='\n')
