from queue import Queue


def read_input(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line


def parse_input(to_q):
    input = read_input("day22.txt")
    if to_q:
        plyr1, plyr2 = Queue(), Queue()
    else:
        plyr1, plyr2 = [], []
    one = True
    for line in input:
        if "Player" in line:
            continue
        if line == "\n":
            one = False
            continue
        if one:
            if to_q:
                plyr1.put(int(line))
            else:
                plyr1.append(int(line))
        else:
            if to_q:
                plyr2.put(int(line))
            else:
                plyr2.append(int(line))
    return plyr1, plyr2


def day22pt1():
    plyr1, plyr2 = parse_input(True)
    while not plyr1.empty() and not plyr2.empty():
        one, two = plyr1.get(), plyr2.get()
        if one > two:
            plyr1.put(one)
            plyr1.put(two)
        else:
            plyr2.put(two)
            plyr2.put(one)

    count = 0
    i = plyr1.qsize() + plyr2.qsize()   # one of them is zero anyway
    while not (plyr2.empty() and plyr1.empty()):
        if plyr1.empty():
            count += i * plyr2.get()
        else:
            count += i * plyr1.get()
        i -= 1
    print(count)


def day22pt2():
    plyr1, plyr2 = parse_input(False)
    history = []
    print(recurse(plyr1, plyr2, history, 1))

    
def recurse(plyr1, plyr2, history, game):
    while str(plyr1) + str(plyr2) not in history and not (len(plyr1) == 0 or len(plyr2) == 0):
        history.append(str(plyr1) + str(plyr2))
        one, two = plyr1.pop(0), plyr2.pop(0)
        if one <= len(plyr1) and two <= len(plyr2):
            if recurse(plyr1[:one], plyr2[:two], [], game+1) == 1:
                plyr1.append(one)
                plyr1.append(two)
            else:
                plyr2.append(two)
                plyr2.append(one)
        else:
            if one > two:
                plyr1.append(one)
                plyr1.append(two)
            else:
                plyr2.append(two)
                plyr2.append(one)

    if game == 1:
        count = 0
        if len(plyr1) == 0:
            for i, num in enumerate(plyr2[::-1]):
                count += (i+1) * num
            return count
        for i, num in enumerate(plyr1[::-1]):
            count += (i+1) * num
        return count

    if len(plyr1) == 0:
        return 2
    return 1


day22pt2()
