from collections import defaultdict
from typing import cast, Iterable


def create_graph(connections_list: Iterable[tuple[str, str]]) -> dict[str, set[str]]:
    connections = defaultdict(set)
    for comp1, comp2 in connections_list:
        connections[comp1].add(comp2)
        connections[comp2].add(comp1)
    return dict(connections)


def part1(connections: dict[str, set[str]]) -> int:
    res = set()
    for k, connected_computers in connections.items():
        other_connected_computers = connected_computers.copy()
        if k.startswith("t"):
            for comp in connected_computers:
                other_connected_computers.remove(comp)
                res.update({tuple(sorted([k, x, comp])) for x in (other_connected_computers & connections[comp])})
    return len(res)


def part2(connections: dict[str, set[str]]) -> str:
    biggest_party = []
    for k, connected_computers in connections.items():
        for comp in connected_computers:
            my_parties = [{k, comp}]
            for other in connected_computers & connections[comp]:
                for party in my_parties:
                    if party.issubset(connections[other]):
                        my_parties.append(party | {other})
            mx = max(my_parties)
            if len(mx) > len(biggest_party):
                biggest_party = mx
    return ",".join(sorted(biggest_party))


def main():
    with open('inputs/day23.txt') as f:
        connections = create_graph(
            cast(tuple[str, str], tuple(x.split('-', 1)))
            for x in f.read().split('\n')
        )
    print(part1(connections))
    print(part2(connections))


if __name__ == '__main__':
    main()
