class Octopus:
    amount_of_flashes = 0

    def __init__(self, value):
        self.last_flash, self.neighbors, self.energy = -1, [], value

    def add_energy(self, day):
        if self.last_flash != day:
            self.energy = 0 if self.energy == 9 else self.energy + 1
            if self.energy == 0:
                self.last_flash = day
                Octopus.amount_of_flashes += 1
                [neighbor.add_energy(day) for neighbor in self.neighbors]


def day10(ipt):
    octopuses = dict()
    for r, row in enumerate(ipt):
        for c, val in enumerate(row):
            this_octopus = octopuses[(r, c)] = Octopus(val)
            for add_r, add_c in [(-1, -1), (-1, 0), (-1, 1), (0, -1)]:
                if (other := octopuses.get((add_r + r, add_c + c), None)) is not None:
                    other.neighbors.append(this_octopus)    # should probably be a method "add_neighbor" but this is shorter :)
                    this_octopus.neighbors.append(other)
    octopuses = octopuses.values()
    day = total_flashes = 0
    while Octopus.amount_of_flashes != len(octopuses):
        total_flashes += Octopus.amount_of_flashes
        if day == 100:
            print(f"part1: { total_flashes }")
        Octopus.amount_of_flashes = 0
        [octopus.add_energy(day) for octopus in octopuses]
        day += 1
    print(f"part2: { day }")


if __name__ == '__main__':
    with open("day11") as input_file:
        day10([[int(x) for x in line.strip()] for line in input_file.readlines()])
        
# idea for faster solution - have an array of len 10 which represents the energy of each octopus. 
# then each day all you need to do is: arr.append(arr.pop(0)), [octopus.move(day) for octopus in arr[-1]]
# move will move it to a -1 index in the array (and check if flashes) [won't affect octopuses in arr[-1]]
