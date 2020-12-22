def day15():
    dic = {}
    input = [2,3,1]
    ln=len(input)
    last=None
    for i,line in enumerate(input):
        if last is not None:
            dic[last] = i
        last = line
    #change the 30000000 to 2020 for part 1
    for num in range(30000000 - ln):
        if last in dic:
            line = ln+num-dic[last] 
        else:
            line=0
        dic[last]=ln+num
        last = line
    print( last)
day15()