def traverse(graph: dict[str, list[str]], node: str, dest: str, cache: dict[str, int]) -> int:
    if node == dest:
        return 1
    if node in cache:
        return cache[node]
    res = 0
    for child in graph[node]:
        res += traverse(graph, child, dest, cache)
    cache[node] = res
    return res


NODE_NAME_TO_FLAG = {"out": 0b001, "dac": 0b010, "fft": 0b100}


def traverse2(
    graph: dict[str, list[str]],
    node: str,
    dest: str,
    cache: dict[str, dict[int, int]]
) -> dict[int, int]:
    if node == dest:
        return {NODE_NAME_TO_FLAG[node]: 1}
    if node in cache:
        return cache[node]
    res = {}
    for child in graph[node]:
        option = traverse2(graph, child, dest, cache)
        for k, v in option.items():
            res[k] = res.get(k, 0) + v
    if node in NODE_NAME_TO_FLAG:
        res = {
            k + NODE_NAME_TO_FLAG[node]: v
            for k, v in res.items()
        }
    cache[node] = res
    return res


def main():
    with open("inputs/day11.txt") as f:
        graph = {line.split(":")[0]: line.split(": ")[1].split(" ") for line in f.read().split("\n")}
        print("part1:", traverse(graph, "you", "out", {}))
        print("part2:", traverse2(graph, "svr", "out", {})[sum(NODE_NAME_TO_FLAG.values())])


main()
