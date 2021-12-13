def part1(arr, instructions):
    instructions = [x.replace('fold along ', '').split('=') for x in instructions]
    for instruction in instructions:
        fold = int(instruction[1])
        if instruction[0] == 'y':
            arr.pop(fold)
            for r in range(len(arr) - fold):
                for c in range(len(arr[0])):
                    arr[fold-1-r][c] = arr[fold-1-r][c] or arr[fold][c]
                arr.pop(fold)
        else:
            [arr[r].pop(fold) for r in range(len(arr))]
            for c in range(len(arr[0]) - fold):
                for r in range(len(arr)):
                    arr[r][fold-1-c] = arr[r][fold-1-c] or arr[r][fold]
                    arr[r].pop(fold)
        if instruction == instructions[0]:
            print(f"part1: { sum(x for line in arr for x in line) }")
    print("part2:")
    for row in arr:
        print(''.join(['#' if x else ' ' for x in row]))


if __name__ == '__main__':
    with open("day13") as input_file:
        dots, instructions = input_file.read().split('\n\n')
    dots = { tuple(map(int, line.strip().split(','))) for line in dots.split('\n') }
    max_y, max_x = max(x[1] for x in dots), max(x[0] for x in dots)
    arr = [[(col, row) in dots for col in range(max_x + 1)] for row in range(max_y + 1)]
    part1(arr, instructions.split('\n'))
