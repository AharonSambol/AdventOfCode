def make_move(blizzards, start, end, board_w, board_h, turn, cache, trips=0):
    q = [(start, turn)]
    while True:
        cur_pos, turn = q.pop(0)
        if (turn, cur_pos) in cache:
            continue
        cache.add((turn, cur_pos))
        if cur_pos == end:
            if trips == 0:
                print('part1:', turn)
            if trips == 2:
                return turn
            return make_move(blizzards, end, start, board_w, board_h, turn, set(), trips + 1)

        if turn != blizzards[1]:
            new_blizzards = {}
            for pos, moves in blizzards[0].items():
                for move in moves:
                    new_pos = (pos[0] + move[0], pos[1] + move[1])
                    if move != (0, 0):
                        new_pos = ((new_pos[0] - 1) % (board_h - 2) + 1, (new_pos[1] - 1) % (board_w - 2) + 1)
                    new_blizzards[new_pos] = new_blizzards.get(new_pos, []) + [move]
            blizzards = (new_blizzards, turn)

        for dr in ((1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)):
            new_dr = (dr[0] + cur_pos[0], dr[1] + cur_pos[1])
            if 0 <= new_dr[0] < board_h and 0 <= new_dr[1] < board_w and new_dr not in blizzards[0]:
                q.append((new_dr, turn + 1))

with open("../Inputs/InputDay24.txt") as file:
    board = file.read().split('\n')
    blizzards = {
        (r, c): [{'#': (0, 0), '>': (0, 1), '<': (0, -1), 'v': (1, 0), '^': (-1, 0)}[val]]
        for r, line in enumerate(board) for c, val in enumerate(line)
        if val != '.'
    }
    start, end = (0, board[0].index('.')), (len(board) - 1, board[-1].index('.'))
    print('part2:', make_move((blizzards, -1), start, end, len(board[0]), len(board), -1, set()))
