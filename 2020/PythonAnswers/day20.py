import re


class Chunk:
    def __init__(self, st):
        self.st = st
        self.sides = get_sides(self.st)
        self.neighbors = None
        self.is_corner = None
        self.is_side = None
        self.is_set = False

    def get_neighbors(self, input, all_chunks):
        neighbors = []
        for chunk2 in input:
            if chunk2 == self.st:
                continue
            sides2 = get_sides(chunk2)
            for side in self.sides:
                if side in sides2 or side[::-1] in sides2:
                    c = get_chunk_obj(chunk2, all_chunks)
                    neighbors.append(c)
        self.neighbors = neighbors
        self.is_corner = len(neighbors) == 2
        self.is_side = len(neighbors) == 3


def read_input_chunks(file_name):
    lst = []
    chunk = ""
    with open(file_name) as in_file:
        for line in in_file:
            if line == "\n":
                lst.append(chunk)
                chunk = ""
            else:
                chunk += line
    return lst


def day20():
    # <for pt two>
    all_chunks = {}
    rand_corner = None
    # </for pt two>

    input = read_input_chunks("day20.txt")
    # <pt one>
    ans_pt_one = 1
    for i, chunk in enumerate(input):
        neighbors = get_neighbors_pt1(i, chunk, input)

        if len(neighbors) == 2:
            first_line = chunk.split("\n")[0]
            ans_pt_one *= int(re.split("[ :]", first_line)[1])
            rand_corner = get_chunk_obj(chunk, all_chunks)    # for pt two
    print("part one:", ans_pt_one)
    # </pt one>
    # <pt two>
    arr = find_tiles_placements(all_chunks, rand_corner, input)
    organize_tiles_rotation(arr)
    picture = combine_arrs(arr)
    for _ in range(2):
        for _ in range(4):
            picture = rotate(picture)
            amount_of_snakes = count_snakes(picture.split("\n"))
            if amount_of_snakes > 1:
                print("part two:", picture.count("#") - (amount_of_snakes*15))
                exit(3141)
        picture = flip(picture)
    print("oh no")


def find_tiles_placements(all_chunks, corner, input):
    arr = [[]]

    # 2 starting tiles
    corner.get_neighbors(input, all_chunks)
    arr[0].append(corner)  # [0][0]
    corner.neighbors[0].get_neighbors(input, all_chunks)
    arr[0].append(corner.neighbors[0])  # [0][1]

    # 2 line one
    while not arr[0][-1].is_corner:
        for nbr in arr[0][-1].neighbors:
            if nbr in arr[0]:
                continue
            nbr.get_neighbors(input, all_chunks)
            if nbr.is_side or nbr.is_corner:
                arr[0].append(nbr)
                break
    # 2 all the rest of the lines
    row = 0
    for i in range(int(len(input) / len(arr[0])) - 1):
        # 2 add new row
        row += 1
        arr.append([])
        # 2 do the first in that row

        for nbr in arr[row - 1][0].neighbors:
            nbr.get_neighbors(input, all_chunks)
            placed_tiles = [x for row in arr for x in row]
            if (nbr.is_side or nbr.is_corner) and nbr not in placed_tiles:
                arr[row].append(nbr)
                break
        for col in range(1, len(arr[0])):
            for nbr in arr[row][col - 1].neighbors:
                placed_tiles = [x for row in arr for x in row]
                if nbr in arr[row - 1][col].neighbors and nbr not in placed_tiles:
                    nbr.get_neighbors(input, all_chunks)
                    arr[row].append(nbr)
                    break
    return arr


def organize_FIRST_tile_rotation(board):
    nbr1, nbr2 = get_sides(board[0][1].st), get_sides(board[1][0].st)
    for _ in range(2):
        for _ in range(4):
            board[0][0].st = rotate(board[0][0])
            chunk = to_arr(board[0][0])
            oneSide = "".join(chunk[- 1])
            secondSide = ""
            for line in chunk:
                secondSide += line[-1]
            if (oneSide in nbr2 or oneSide[::-1] in nbr2) and \
                    (secondSide in nbr1 or secondSide[::-1] in nbr1):
                board[0][0].is_set = True
                return
        board[0][0].st = flip(board[0][0])
    print("!!!!!!!! OH FUDGING BLUE UNICORNS !!!!!!!!!!!!!!!!!!!!!")
    exit(-31415926)


def organize_tiles_rotation(board):
    organize_FIRST_tile_rotation(board)
    for row, line in enumerate(board):
        for col, chunk in enumerate(line):
            if row == 0 and col == 0:
                continue
            nbr1 = chunk.neighbors[0]
            i = 1
            while not nbr1.is_set:
                nbr1 = chunk.neighbors[i]
                i += 1
            plcX1, plcY1 = get_pos(board, row, col, nbr1)
            sides_mine, sides1 = get_sides(chunk.st), get_sides(nbr1.st)

            shared_side1 = None
            for side in sides_mine:
                if side in sides1:
                    shared_side1 = side
                elif side[::-1] in sides1:
                    shared_side1 = side[::-1]

            orient(board, row, col, shared_side1, plcX1, plcY1)
            board[row][col].is_set = True
    print("done")


def orient(board, row, col, shared_side1, plc_x, plc_y):
    for _ in range(2):
        for _ in range(4):
            board[row][col].st = rotate(board[row][col])

            if is_valid(board, row, col, shared_side1, plc_x, plc_y):
                return
        board[row][col].st = flip(board[row][col])
    print("!!!!!!!! OH FUDGING BLUE UNICORNS !!!!!!!!!!!!!!!!!!!!!")
    exit(-31415926)


def flip(chunk):
    chunk = to_arr(chunk)
    new_arr = [[None] * len(chunk) for _ in range(len(chunk[0]))]
    for r in range(len(chunk)):
        for c in range(len(chunk[0])):
            new_arr[c][r] = chunk[r][c]
    return to_st(new_arr)


def rotate(chunk):
    chunk = to_arr(chunk)
    new_arr = [[None] * len(chunk) for _ in range(len(chunk[0]))]

    for c in range(len(chunk[0])):
        for r in range(len(chunk)):
            new_arr[c][r] = chunk[len(chunk)-1-r][c]
    return to_st(new_arr)


def to_arr(chunk):
    st = chunk
    if str(chunk) != chunk:
        st = chunk.st
    chunk = list(filter(lambda x: "Tile" not in x and x != "", st.split("\n")))
    return [list(line) for line in chunk]


def to_st(arr):
    st = ""
    for line in arr:
        for ch in line:
            st += ch
        st += "\n"
    return st[:-1]


def get_pos(board, row, col, looking_for):
    try:
        if board[row+1][col] == looking_for:
            return 1, 0
    except IndexError:
        pass
    try:
        if board[row][col+1] == looking_for:
            return 0, 1
    except IndexError:
        pass
    try:
        if board[row-1][col] == looking_for:
            return -1, 0
    except IndexError:
        pass
    return 0, -1


def is_valid(board, row, col, shared_side1, plc_x, plc_y):
    chunk = to_arr(board[row][col])
    if plc_x == 1 and plc_y == 0:   # \/
        if "".join(chunk[len(chunk)-1]) != shared_side1:
            return False
    elif plc_x == 0 and plc_y == 1:    # ->
        st = ""
        for row in chunk:
            st += row[len(row)-1]
        if st != shared_side1:
            return False
    elif plc_x == -1 and plc_y == 0:    # ^
        if "".join(chunk[0]) != shared_side1:
            return False
    else:    # <-
        st = ""
        for row in chunk:
            st += row[0]
        if st != shared_side1:
            return False
    return True


def get_chunk_obj(chunk_st, all_chunks):
    if chunk_st in all_chunks:
        return all_chunks[chunk_st]
    all_chunks[chunk_st] = Chunk(chunk_st)
    return all_chunks[chunk_st]


def get_neighbors_pt1(i, chunk, input):
    neighbors = []
    sides = get_sides(chunk)
    for j, chunk2 in enumerate(input):
        if i == j:
            continue
        sides2 = get_sides(chunk2)
        for side in sides:
            if side in sides2 or side[::-1] in sides2:
                neighbors.append(chunk2)
    return neighbors


def get_sides(chunk):
    chunk = list(filter(lambda x: x != "" and "Tile" not in x, chunk.split("\n")))
    sides = [chunk[0].strip(), chunk[-1].strip()]
    side1, side2 = "", ""
    for row in chunk:
        side1 += row[0]
        side2 += row[-1]
    sides.append(side1), sides.append(side2)
    return sides


def combine_arrs(arr):
    new_arr = []
    for row in arr:
        chunk_arr = []
        for chunk in row:
            to_app = list(filter(lambda x: x != "" and "Tile" not in x, chunk.st.split("\n")))
            to_app.pop(0), to_app.pop(-1)
            to_app = [a[1:-1] for a in to_app]
            chunk_arr.append(to_app)
        new_arr.append(chunk_arr)
    arr = new_arr
    for row in range(len(arr)):
        for col in range(1, len(arr[0])):
            for line in range(len(arr[row][col])):
                arr[row][0][line] += arr[row][col][line]
    st = ""
    for row in range(len(arr)):
        for line in range(len(arr[row][0])):
            st += arr[row][0][line]
            st += "\n"
    return st


def count_snakes(arr):
    count = 0
    for row in range(len(arr)):
        for col in range(len(arr[row])):
            try:
                if "#" == arr[row][col] == arr[row-1][col+18] == arr[row+1][col+1] == arr[row+1][col+4] ==\
                        arr[row][col+5] == arr[row][col+6] == arr[row+1][col+7] == arr[row+1][col+10] == \
                        arr[row][col+11] == arr[row][col+12] == arr[row+1][col+13] == arr[row+1][col+16] == \
                        arr[row][col+17] == arr[row][col+18] == arr[row][col+19]:
                    count += 1
            except IndexError:
                pass
    return count


day20()
