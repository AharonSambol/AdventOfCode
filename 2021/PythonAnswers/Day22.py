import re
from dataclasses import dataclass
import math

class Cube:
    def __init__(self, top, bottom):
        self.top, self.bottom = top, bottom
    
    def intersects(self, other):
        for i in ['x', 'y', 'z']:
            for c1, c2 in [(self, other), (other, self)]:
                if c1.top.__dict__[i] < c2.bottom.__dict__[i]:
                    return False
        return True

    def split(self, o_top, o_bottom):
        up_layer = bottom_layer = right_layer = left_layer = front_layer = back_layer =  None
        top, bottom = self.top, self.bottom
        if o_top.y < self.top.y:
            up_layer = Cube(self.top, Pos(self.bottom.dr, o_top.y + 1, self.bottom.z))
            top = Pos(self.top.dr, up_layer.bottom.y - 1, self.top.z)
        if o_bottom.y > self.bottom.y:
            bottom_layer = Cube(Pos(self.top.dr, o_bottom.y - 1, self.top.z), self.bottom)
            bottom = Pos(self.bottom.dr, bottom_layer.top.y + 1, self.bottom.z)
        if o_top.dr < self.top.dr:
            right_layer = Cube(top, Pos(o_top.dr + 1, bottom.y, bottom.z))
            top = Pos(right_layer.bottom.dr - 1, top.y, top.z)
        if o_bottom.dr > self.bottom.dr:
            left_layer = Cube(Pos(o_bottom.dr - 1, top.y, top.z), bottom)
            bottom = Pos(left_layer.top.dr + 1, bottom.y, bottom.z)
        if o_top.z < self.top.z:
            front_layer = Cube(top, Pos(bottom.x, bottom.y, o_top.z + 1))
        if o_bottom.z > self.bottom.z:
            back_layer = Cube(Pos(top.x, top.y, o_bottom.z - 1), bottom)
        all_new = [up_layer, bottom_layer, right_layer, left_layer, back_layer, front_layer]
        return [new_block for new_block in all_new if new_block]

@dataclass
class Pos:
    x: int
    y: int
    z: int

def add_cube(cubes, new_cube, command):
    new_cubes = [new_cube] if command == 'on' else []
    for cube in cubes:
        if cube.intersects(new_cube):
            new_cubes.extend(cube.split(new_cube.top, new_cube.bottom))
        else:
            new_cubes.append(cube)
    return new_cubes

def calc_res(cubes, res=0):
    for cube in cubes:
        res += math.prod([abs(cube.bottom.__dict__[x] - cube.top.__dict__[x]) + 1 for x in ['x', 'y', 'z']])
    return res

def part2(instructions, is_part1):
    cubes = []
    for command, line in instructions:
        x_rng, y_rng, z_rng = (list(map(int, rng.split('..'))) for rng in re.findall(r'-?\d+\.\.-?\d+', line)) 
        new_cube = Cube(Pos(x_rng[1], y_rng[1], z_rng[1]), Pos(x_rng[0], y_rng[0], z_rng[0]))    
        cubes = add_cube(cubes, new_cube, command)
    if is_part1:
        return calc_res(cubes) - calc_res(add_cube(cubes, Cube(Pos(50,50,50), Pos(-50,-50,-50)), 'off'))
    return calc_res(cubes)


with open('/home/aharonsambol/code/advent/day22.txt') as input_file:
    ipt = [line.split() for line in input_file.readlines()]
print(part2(ipt, True))
print(part2(ipt, False))
