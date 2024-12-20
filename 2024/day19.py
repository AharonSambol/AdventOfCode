from __future__ import annotations

from dataclasses import dataclass

cache = {}


@dataclass
class Node:
    children: dict[str, Node]
    is_end: bool = False


def create_tri(towels: list[str]) -> Node:
    base = Node({})
    for towel in towels:
        pointer = base
        for stripe in towel:
            if stripe not in pointer.children:
                pointer.children[stripe] = Node({})
            pointer = pointer.children[stripe]
        pointer.is_end = True
    return base


def num_of_solutions(pattern: str, tri: Node) -> int:
    if pattern in cache:
        return cache[pattern]
    res = 0
    pointer = tri
    for i, color in enumerate(pattern):
        if color not in pointer.children:
            cache[pattern] = res
            return res
        pointer = pointer.children[color]
        if pointer.is_end:
            res += num_of_solutions(pattern[i + 1:], tri)
    cache[pattern] = res + pointer.is_end
    return res + pointer.is_end


def part1(towels: Node, patterns: list[str]) -> int:
    return sum(num_of_solutions(pattern, towels) != 0 for pattern in patterns)


def part2(towels: Node, patterns: list[str]) -> int:
    return sum(num_of_solutions(pattern, towels) for pattern in patterns)


def main():
    with open('inputs/day19.txt') as f:
        towels, patterns = f.read().split('\n\n')
        towels = create_tri(towels.split(", "))
        patterns = patterns.split("\n")
    print(part1(towels, patterns))
    print(part2(towels, patterns))


if __name__ == '__main__':
    main()
