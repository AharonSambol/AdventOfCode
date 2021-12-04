import re


def board_won_short_version(board, seen_nums):
    return any(all(x in seen_nums for x in row) for row in board + list(zip(*board[::-1])))


def board_won(board, seen_nums):
    rotated_board = list(zip(*board[::-1]))
    for row in board + rotated_board:
        if all(x in seen_nums for x in row):
            return True
    return False


def day4(part1):
    with open("day4") as input_file:
        input_data = input_file.read().split('\n\n')
        numbers = input_data.pop(0).split(',')
        # make an matrix of [board[row[value]]]
        boards = [[re.split(' +', row.strip()) for row in board.split('\n')] for board in input_data]

        seen_nums = set()
        for num in numbers:
            seen_nums.add(num)
            for b, board in enumerate(boards):
                if board_won(board, seen_nums):
                    sm = sum(int(val) for row in board for val in row if val not in seen_nums)
                    if part1:
                        return sm * int(num)
                    else:
                        boards.pop(b)
                        if len(boards) == 0:
                            return sm * int(num)


print(f"solution for part1: { day4(True) }")
print(f"solution for part2: { day4(False) }")
