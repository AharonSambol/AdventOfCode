part1 = False
with open("../Inputs/InputDay06.txt") as file:
    datastream = file.read()
    ln = 4 if part1 else 14
    a = [datastream[0]] * ln
    for i, x in enumerate(datastream):
        a[i % ln] = x
        if len(set(a)) == ln:
            print(i + 1)
            break
