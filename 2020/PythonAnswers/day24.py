import copy
import re


def read_input(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def day24pt1():
    input = [re.findall("(e|se|sw|nw|w|ne)", line) for line in read_input("day24.txt")]
    arr = [[False] * 1000 for _ in range(1000)]

    for line in input:
        posX, posY = 500, 500
        for dir in line:
            if dir == "e":
                posY += 1
                posX += 3
            elif dir == "se":
                posY += 3
                posX += 2
            elif dir == "sw":
                posY += 2
                posX -= 1
            elif dir == "nw":
                posY -= 3
                posX -= 2
            elif dir == "w":
                posY -= 1
                posX -= 3
            elif dir == "ne":
                posY -= 2
                posX += 1
        arr[posX][posY] = not arr[posX][posY]

    print(str(arr).count("True"))
    return arr


def day24pt2():
    arr = day24pt1()
    new_arr = [[False] * 1000 for _ in range(1000)]
    for _ in range(100):
        area_to_check = get_area(arr)
        for r in range(area_to_check["sr"], area_to_check["br"]):
            for c in range(area_to_check["sc"], area_to_check["bc"]):
                nbrs = get_neighbors(arr, r, c)
                if arr[r][c]:
                    if nbrs == 0 or nbrs > 2:
                        pass
                    else:
                        new_arr[r][c] = True
                else:
                    if nbrs == 2:
                        new_arr[r][c] = True
        arr = copy.deepcopy(new_arr)
        new_arr = [[False] * 1000 for _ in range(1000)]

    print(str(arr).count("True"))


def get_neighbors(arr, posX, posY):
    ans = [arr[posX + 3][posY + 1], arr[posX + 2][posY + 3], arr[posX - 1][posY + 2], arr[posX - 2][posY - 3],
           arr[posX - 3][posY - 1], arr[posX + 1][posY - 2]]
    return str(ans).count("True")


def get_area(arr):    # I shouldn't do each tile only the valid ones (like pos 500,501 isn't an actual tile)
    smallest_row = len(arr)
    smallest_col = len(arr)
    biggest_row = 0
    biggest_col = 0

    for r in range(len(arr)):
        for c in range(len(arr[0])):
            if arr[r][c]:
                if r < smallest_row:
                    smallest_row = r
                if c < smallest_col:
                    smallest_col = c
                if r > biggest_row:
                    biggest_row = r
                if c > biggest_col:
                    biggest_col = c
    return {"sr": smallest_row-3,
            "sc": smallest_col-3,
            "br": biggest_row+3,
            "bc": biggest_col+3}


day24pt2()
