from __future__ import annotations

from typing import Optional

Node = int | str | list


def parse_registers(content: str) -> dict[str, int]:
    res = {}
    for register in content.split("\n"):
        register = [x.rstrip(":") for x in register.split(" ")[1:]]
        res[register[0]] = int(register[1])
    return res


def combo(registers: dict[str, str | int], num: int) -> str | int:
    return num if num < 4 else registers["ABC"[num - 4]]


def part1(registers: dict[str, int], program: list[int]) -> str:
    pointer = 0
    out = []
    while pointer + 1 < len(program):
        operator, operand = program[pointer: pointer + 2]
        match operator:
            case 0:
                registers["A"] //= 2 ** combo(registers, operand)
            case 1:
                registers["B"] ^= operand
            case 2:
                registers["B"] = combo(registers, operand) % 8
            case 3:
                if registers["A"] != 0:
                    pointer = operand
                    continue
            case 4:
                registers["B"] ^= registers["C"]
            case 5:
                out.append(combo(registers, operand) % 8)
            case 6:
                registers["B"] = registers["A"] // (2 ** combo(registers, operand))
            case 7:
                registers["C"] = registers["A"] // (2 ** combo(registers, operand))
        pointer += 2
    return ",".join(str(x) for x in out)


def to_str(x: Node) -> str:
    if not isinstance(x, list):
        return str(x)
    return "(" + "".join(to_str(a) for a in x) + ")"


def part2(registers: dict[str:int], program: list[int]) -> int:
    registers = {k: "x" if k == "A" else str(v) for k, v in registers.items()}
    possibilities = []
    _part2(registers, program, 0, program, [], possibilities)

    all_changes = []
    for equation in possibilities[0]:
        orig = to_str(equation)
        changes = []
        get_changes(equation, changes)
        all_changes.append((min(changes, default=1), orig))
    all_changes.sort(reverse=True, key=lambda item: item[0])
    x = 0
    while True:
        for change, equation in all_changes:
            if not eval(equation):
                x += change
                break
        else:
            return x


def try_calc(a: int | str, op: str, b: int | str) -> Node:
    match a, op, b:
        case [a1, "//", int(a2)], "//", int():
            return [a1, '//', a2 * b]
        case int(), "**", int():
            return a ** b
        case int(), "//", int():
            return a // b
        case int(), "^", int():
            return a ^ b
        case int(), "%", int():
            return a % b
        case _:
            return [a, op, b]


def get_changes(equation: Node, changes: list[int]) -> bool:
    if equation == "x":
        return True
    if not isinstance(equation, list):
        return False
    if len(equation) == 1:
        return get_changes(equation[0], changes)
    for i, x in enumerate(equation):
        if get_changes(x, changes):
            match equation[i + 1: i + 3]:
                case ["//", int(divider)]:
                    changes.append(divider)
                case _:
                    changes.append(1)
                    return False
    return False


def _part2(
    registers: dict[str, Node],
    program: list[int],
    pointer: int,
    expected_out: list[int],
    conditions: list[Node],
    possibilities: list[list[Node]]
) -> Optional[str]:
    while pointer + 1 < len(program):
        operator, operand = program[pointer: pointer + 2]
        match operator:
            case 0:
                registers["A"] = try_calc(registers["A"], "//", try_calc(2, "**", combo(registers, operand)))
            case 1:
                registers["B"] = try_calc(registers["B"], "^", int(operand))
            case 2:
                registers["B"] = try_calc(combo(registers, operand), "%", 8)
            case 3:
                _part2(
                    registers.copy(),
                    program,
                    operand,
                    expected_out,
                    conditions + [[registers["A"], "!=", 0]],
                    possibilities,
                )
                conditions.append([registers["A"], "==", 0])
            case 4:
                registers["B"] = try_calc(registers["B"], "^", registers["C"])
            case 5:
                if not expected_out:
                    return
                conditions.append(
                    [try_calc(combo(registers, operand), "%", 8), "==", expected_out[0]]
                )
                expected_out = expected_out[1:]
            case 6 | 7:
                registers[{6: "B", 7: "C"}[operator]] = try_calc(
                    registers["A"], "//", try_calc(2, "**", combo(registers, operand))
                )
        pointer += 2
    if not expected_out:
        possibilities.append(conditions)


def main():
    with open("inputs/day17.txt") as f:
        registers, program = f.read().split("\n\n")
        registers = parse_registers(registers)
        program = [int(x) for x in program.lstrip("Program: ").split(",")]
    print(part1(registers.copy(), program))
    print(part2(registers, program))


if __name__ == "__main__":
    main()
