def part1(lines: list[list[str]]) -> int:
    xmases = [list("XMAS"), list("SAMX")]
    return sum(
        (
            (line[c: c + 4] in xmases)
            + ([line[c] for line in lines[r: r + 4]] in xmases)
            + (c + 3 < len(line) and [line[c + i] for i, line in enumerate(lines[r: r + 4])] in xmases)
            + (c > 2 and ([line[c - i] for i, line in enumerate(lines[r: r + 4])] in xmases))
        )
        for r, line in enumerate(lines)
        for c, item in enumerate(line)
    )


def part2(lines: list[list[str]]) -> int:
    return sum(
        (
            item == "A"
            and {"M", "S"}
            == {lines[r - 1][c - 1], lines[r + 1][c + 1]}
            == {lines[r + 1][c - 1], lines[r - 1][c + 1]}
        )
        for r, line in enumerate(lines[1:-1], start=1)
        for c, item in enumerate(line[1:-1], start=1)
    )


def main():
    with open("inputs/day04.txt") as f:
        lines = [list(line) for line in f.read().split("\n")]
        print(part1(lines))
        print(part2(lines))


if __name__ == '__main__':
    main()
