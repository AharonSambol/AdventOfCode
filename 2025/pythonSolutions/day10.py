import itertools
import string
from typing import Any

from z3 import Int, Optimize


def solve_part1(equations: list[tuple[bool, list[bool]]], possible_options: list[list[int]]) -> int:
    return next(
        sum(option)
        for option in possible_options
        if all(
            sum(mask and opt for mask, opt in zip(button_mask, option)) % 2 == goal
            for goal, button_mask in equations
        )
    )


def part1(lines: list[list[str]]) -> None:
    res = 0
    for goal, *buttons, voltages in lines:
        possible_options = sorted(itertools.product([0, 1], repeat=len(buttons)), key=lambda x: sum(x))
        equations = [(g == '#', [False] * len(buttons)) for g in goal[1:-1]]

        init_buttons(buttons, equations)
        res += solve_part1(equations, possible_options)
    print("part1:", res)


def solve_part2(equations: list[tuple[int, list[bool]]]) -> int:
    variables = [Int(letter) for letter, _ in zip(string.ascii_letters, equations[0][1])]
    solver = Optimize()
    for var in variables:
        solver.add(var >= 0)
    for goal, equation in equations:
        solver.add(int(goal) == sum(x for x, m in zip(variables, equation) if m))
    solver.minimize(sum(variables))
    solver.check()
    model = solver.model()
    return sum(int(model[var].as_long()) for var in variables)


def part2(lines: list[list[str]]) -> None:
    res = 0
    for goal, *buttons, voltages in lines:
        equations = [(int(voltage), [False] * len(buttons)) for voltage in voltages[1:-1].split(",")]
        init_buttons(buttons, equations)
        res += solve_part2(equations)
    print("part2:", res)


def init_buttons(buttons: list[str], equations: list[tuple[Any, list[bool]]]) -> None:
    for button_index, button in enumerate(buttons):
        for affected_light in button[1:-1].split(","):
            equations[int(affected_light)][1][button_index] = True


def main():
    with open("inputs/day10.txt") as f:
        lines = [line.split(" ") for line in f.read().split("\n")]
        part1(lines)
        part2(lines)


if __name__ == '__main__':
    main()
