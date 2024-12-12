from __future__ import annotations

import copy
from typing import Callable

Pos = tuple[int, int]


class Region:
    def __init__(self, typ: str, pos: Pos):
        self.typ = typ
        self.fences = 4
        self.flower_count = 1
        self.neighbors: set[Region] = set()
        self.posses = {pos}
        self.pos = pos

    def __hash__(self):
        return self.pos.__hash__()

    def take_over_other_region(self, other_region: Region, garden: list[list[str | Region]]):
        self.posses.update(other_region.posses)
        self.neighbors.update(other_region.neighbors)
        self.flower_count += other_region.flower_count
        self.fences += other_region.fences
        for pos_r, pos_c in other_region.posses:
            garden[pos_r][pos_c] = self


def calculate_new_fences_part1(amount_of_same_neighbors: int, _, __) -> int:
    return 2 if amount_of_same_neighbors == 1 else 0


def calculate_new_fences_part2(amount_of_same_neighbors: int, pos: Pos, region_posses: set[Pos]) -> int:
    r, c = pos
    if amount_of_same_neighbors == 1:
        amount_of_diagonals = (
            ((r - 1, c - 1) in region_posses)
            + ((r - 1, c) in region_posses and (r - 1, c + 1) in region_posses)
        )
        return amount_of_diagonals * 2
    return 0 if (r - 1, c + 1) in region_posses else -2


def solve(garden: list[list[str | Region]], calculate_new_fences: Callable[[int, Pos, set[Pos]], int]) -> int:
    regions = set()
    for r, row in enumerate(garden):
        for c, flower in enumerate(row):
            neighbors = [x for x in (r > 0 and garden[r - 1][c], c > 0 and garden[r][c - 1]) if x]
            same_typ_neighbors = [neighbor for neighbor in neighbors if neighbor.typ == flower]
            diff_typ_neighbors = [neighbor for neighbor in neighbors if neighbor.typ != flower]
            if same_typ_neighbors:
                region = row[c] = same_typ_neighbors[0]
                region.flower_count += 1
                region.posses.add((r, c))
                region.fences += calculate_new_fences(len(same_typ_neighbors), (r, c), region.posses)
                if region is not (other_region := same_typ_neighbors[-1]):
                    region.take_over_other_region(other_region, garden)
                    regions.remove(other_region)
            else:
                region = row[c] = Region(flower, (r, c))
                regions.add(region)

            for neighbor in diff_typ_neighbors:
                region.neighbors.add(neighbor)
                neighbor.neighbors.add(region)

    return sum(region.fences * region.flower_count for region in regions)


def main():
    with open('inputs/day12.txt') as f:
        garden = [list(line) for line in f.read().split('\n')]
    assert solve(copy.deepcopy(garden), calculate_new_fences_part1) == 1402544
    assert solve(garden, calculate_new_fences_part2) == 862486


if __name__ == '__main__':
    main()