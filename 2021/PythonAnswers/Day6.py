with open("day6") as input_file:
    input_data = input_file.read()
    fish = [input_data.count(str(i)) for i in range(9)]
    for _ in range(256):
        fish.append(to_add := fish.pop(0))
        fish[6] += to_add
    print(sum(fish))
