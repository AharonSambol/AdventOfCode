import itertools
import multiprocessing
import re


class Graph:
    def __init__(self, p, ns):
        self.pressure = int(p)
        self.neighbors = ns
        self.distances = {n: 1 for n in ns}

def get_dist(graph, name, looking_for, visited):
    if dest == name:
        return 0
    if dest in graph[name].distances:
        return graph[name].distances[dest]
    for neighbor in graph[name].neighbors:
        if neighbor in visited:
            continue
        rs = get_dist(graph, neighbor, looking_for, visited | {neighbor})
        if rs:
            rs += 1
            if name in graph[looking_for].distances:
                rs = min(graph[looking_for].distances[name], rs)
            graph[name].distances[looking_for] = rs
            graph[looking_for].distances[name] = rs

    return False

def solve1(graph, pos, visited, time):
    mx = 0
    for name in graph:
        if name in visited or graph[name].pressure == 0:
            continue
        distance = graph[pos].distances.get(name, 0)
        if time > distance + 2:
            sol = solve1(
                graph, name, visited | {name},
                time - distance - 1,
            )
            mx = max(mx, (time - distance - 1) * graph[name].pressure + sol)
    return mx

def solve2(pos1, pos2, destinations, time):
    if time < 0:
        return 0
    mx = 0
    if time == pos1[1] == pos2[1]:
        for name1 in destinations:
            destinations.remove(name1)
            for name2 in destinations:
                if name1 == name2:
                    continue
                destinations.remove(name2)
                o_o = graph[pos1[0]].distances.get(name1, 0)
                o_t = graph[pos1[0]].distances.get(name2, 0)
                t_o = graph[pos2[0]].distances.get(name1, 0)
                t_t = graph[pos2[0]].distances.get(name2, 0)
                o_o, t_t, o_t, t_o = map(lambda x: time - x - 1, (o_o, t_t, o_t, t_o))
                clac_route = lambda d1, d2: \
                    solve2((name1, d1), (name2, d2), destinations, max(d1, d2))\
                        + sum(graph[n].pressure * max(0, d) for n, d in ((name1, d1), (name2, d2)))
                if not (o_o <= t_o and t_t <= o_t):
                    mx = max(clac_route(o_o, t_t), mx)
                if not (o_o > t_o and t_t > o_t):
                    mx = max(clac_route(t_o, o_t), mx)
                destinations.add(name2)
            destinations.add(name1)
        return mx
    from_, other = (pos1[0], pos2) if pos1[1] == time else (pos2[0], pos1)
    for name in destinations:
        d = graph[from_].distances.get(name, 0)
        d = time - d - 1
        add = 0 if d <= 0 else graph[name].pressure * d
        mx = max(mx, add + solve2((name, d), other, destinations - {name}, max(d, other[1])))
    return mx

with open("../Inputs/InputDay16.txt") as file:
    graph = {}
    for line in file:
        name, pressure, *lead_to = re.findall(r".([A-Z]+|\d+)", line)
        graph[name] = Graph(pressure, lead_to)
    for name in graph:
        for dest in graph:
            get_dist(graph, name, dest, set(name))

    destinations = {x for x in graph if graph[x].pressure > 0}

    print('part1:', solve1(graph, 'AA', set(), 30))
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # !!! WARNING part 2 takes a lot of time and uses all processors !!!
    # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    exit(9)
    with multiprocessing.Pool() as pool:
        threads = []
        mx = 0
        for name1 in destinations:
            for name2 in destinations:
                if name1 == name2:
                    continue
                dests = destinations - { name1, name2 }
                d1 = 25 - graph['AA'].distances.get(name1, 0)
                d2 = 25 - graph['AA'].distances.get(name2, 0)
                threads.append((
                    sum(graph[n].pressure * d for n, d in ((name1, d1), (name2, d2))),
                    pool.apply_async(solve2, ((name1, d1), (name2, d2), destinations, max(d1, d2)))
                ))
        print(max(x + y.get() for x, y in threads))
    # print('part2:', solve2(('AA', 26), ('AA', 26), destinations, 26))


