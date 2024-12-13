from __future__ import annotations
import itertools
import time
from dataclasses import dataclass
from typing import Optional


def part1(data: list[int]) -> int:
    start, end = 0, len(data) - 1
    if end % 2 != 0:
        end -= 1
    res = pos = 0
    while start <= end:
        if start % 2 == 0:
            for _ in range(data[start]):
                res += start // 2 * pos
                pos += 1
            data[start] = 0
        else:
            for _ in range(data[start]):
                while data[end] == 0:
                    end -= 2
                    if end < start:
                        return res
                data[end] -= 1
                res += pos * (end // 2)
                pos += 1
        start += 1
    return res


def part2(data: list[int]) -> int:
    @dataclass
    class Node:
        val: int
        pos: int
        len: int
        prev: Optional[Node]
        next: Optional[Node] = None

    nodes_to_try_to_move = []
    pointer = head = None
    pos = 0
    for i, (space, fill) in enumerate(zip(itertools.chain([0], data[1::2]), data[::2])):
        node = Node(val=i, pos=pos + space, len=fill, prev=pointer)
        if head is None:
            pointer = head = node
        else:
            pointer.next = node
            pointer = node
        pos += space + fill
        nodes_to_try_to_move.append(node)

    failed = None
    for node in nodes_to_try_to_move[1:][::-1]:
        pointer = head
        if failed and failed <= node.len:
            continue
        while pointer.next and pointer is not node:
            if pointer.next.pos - pointer.pos - pointer.len >= node.len:
                # remove from list
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev
                # add to list
                if pointer.next:
                    pointer.next.prev = node
                node.prev, node.next = pointer, pointer.next
                pointer.next = node
                # update pos
                node.pos = pointer.pos + pointer.len
                break
            pointer = pointer.next
        else:
            if failed is None or failed > node.len:
                failed = node.len
    res = 0
    while head:
        for i in range(head.pos, head.pos + head.len):
            res += head.val * i
        head = head.next
    return res


def main():
    with open('inputs/day09.txt') as f:
        data = [int(x) for x in f.read()]
    print(part1([x for x in data]))
    print(part2(data))


if __name__ == '__main__':
    main()
