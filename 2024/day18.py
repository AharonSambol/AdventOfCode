from typing import Optional, cast


def solve_maze(board: dict[tuple[int, int], bool]) -> Optional[int]:
    pos = (0, 0)
    end = (70, 70)
    queue = [(pos, 0)]
    visited = set()
    while queue:
        pos, cost = queue.pop(0)
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            new_pos = (pos[0] + dr, pos[1] + dc)
            if new_pos == end:
                return cost + 1
            if new_pos in board or new_pos in visited:
                continue
            if new_pos[0] in range(end[0] + 1) and new_pos[1] in range(end[1] + 1):
                queue.append((new_pos, cost + 1))
                visited.add(new_pos)
    return None


def part1(content: list[tuple[int, int]]) -> int:
    board = {}
    for byte in content[:1024]:
        board[byte] = False
    return solve_maze(board)


def part2(content: list[tuple[int, int]]) -> str:
    board = {}
    for byte in content[:1024]:
        board[byte] = False
    start = 1024
    end = len(content)
    while end - start > 1:
        temp_board = board.copy()
        temp_end = start + (end - start) // 2
        for byte in content[start:temp_end]:
            temp_board[byte] = False
        can_solve = solve_maze(temp_board)
        if can_solve:
            board = temp_board
            start = temp_end
        else:
            end = temp_end
    return ",".join(str(x) for x in content[start])


def main():
    with open('inputs/day18.txt') as f:
        content = [
            cast(tuple[int, int], tuple(int(x) for x in line.split(',', 1)))
            for line in f.read().split('\n')
        ]
    print(part1(content))
    print(part2(content))


if __name__ == '__main__':
    main()
