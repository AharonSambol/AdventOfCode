#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#the difference between part one and part two is only the posW and for w in range
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class cube:
    def _init_(self, posX, posY, posZ, posW):
        self.posX = posX
        self.posY = posY
        self.posZ = posZ
        self.posW = posW
        self.state = False
        
    def turn_on(self, all_cubes):
        self.state = True
        self.make_neighbours(all_cubes)
        
    def get_neighbours(self,all_cubes):
        self.neighbours = get_all_neighbours(all_cubes, self.posX, self.posY, self.posZ, self.posW)
    
    def make_neighbours(self,all_cubes):
        self.neighbours = make_neighbours(all_cubes, self.posX, self.posY, self.posZ, self.posW)

def day17():
    all_cubes = {}
    with open("day17.txt") as in_file:
        for y,line in enumerate(in_file):
            for x,char in enumerate(line):
                if char == "\n":
                    continue
                cube = add_cube(all_cubes, x, y, 0, 0)
                if char == "#":
                    cube.turn_on(all_cubes)
    for _ in range(6):
        print("-------------------------")
        new_all_cubes = []
        for key in all_cubes:
            cube = all_cubes[key]
            # count amount of neighbours which are on
            cube.get_neighbours(all_cubes)
            amount_of_on_neighbours = 0
            for n in cube.neighbours:
                if n.state:
                    amount_of_on_neighbours += 1
            #if cube is on
            if cube.state:
                if amount_of_on_neighbours==2 or amount_of_on_neighbours==3:
                    new_all_cubes.append(cube)
            #if cube is off
            else:
                if amount_of_on_neighbours==3:
                    new_all_cubes.append(cube)
        all_cubes={}
        for cube in new_all_cubes:
            all_cubes[str(cube.posX)+","+str(cube.posY)+","+str(cube.posZ)+","+str(cube.posW)] = cube
            cube.turn_on(all_cubes)
        
    count = 0
    for cube in all_cubes:
        if all_cubes[cube].state:
            count+=1
    print(count)
        
def add_cube(all_cubes,x,y,z,w):
    pos = str(x)+","+str(y)+","+str(z)+","+str(w)
    if pos not in all_cubes:
        all_cubes[pos] = cube(x,y,z,w)
    return all_cubes[pos]
    
    
def make_neighbours(all_cubes, posX, posY, posZ, posW):
    neighbours = []
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if not (x==0 and y==0 and z==0 and w==0):
                        neighbours.append(add_cube(all_cubes,posX+x,posY+y,posZ+z,posW+w))
    return neighbours
		
def get_all_neighbours(all_cubes, posX, posY, posZ, posW):
    neighbours = []
    for x in range(-1,2):
        for y in range(-1,2):
            for z in range(-1,2):
                for w in range(-1,2):
                    if not (x==0 and y==0 and z==0 and w==0):
                        pos = str(posX+x)+","+str(posY+y)+","+str(posZ+z)+","+str(posW+w)
                        if pos in all_cubes:
                            neighbours.append(all_cubes[pos])
    return neighbours
		
    
day17()