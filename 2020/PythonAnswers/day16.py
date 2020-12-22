import re

def read_input_chunks(file_name):
    with open(file_name) as in_file:
        for line in in_file:
            yield line
            
            
def day16():
    count = 0
    skip = False
    adding_ranges = True
    valid_nums = [False]*1000
    all_ranges = {}
    rang_to_name = {}
    my_ticket = []
    valid_tickets = []
    input = read_input_chunks("day16.txt")
    for line in input:
        if "your ticket:" in line:
            skip=True
            continue
        if "nearby tickets:" in line:
            adding_ranges = False
            continue
        if skip:
            #for pt 2
            my_ticket = re.split("[,\n]",line)
            my_ticket = list(filter(lambda x: (x is not ""),my_ticket))
            
            skip=False
            continue    
        if re.match("\n",line):
            continue
        if adding_ranges:    
            ranges = re.split("(?:.*: | or |\n)",line)
            ranges = list(filter(lambda x: (x is not ""),ranges))
            
            #for pt 2
            all_ranges[str(ranges)] = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
            rang_to_name[str(ranges)] = re.split(":",line)[0]
            
            for range_nums in ranges:
                range_nums=range_nums.split("-")
                for i in range(int(range_nums[0]),int(range_nums[1])+1):
                    valid_nums[i]=True
        else:
            nums = re.split("[,\n]",line)
            nums = list(filter(lambda x: (x is not ""),nums))
            #for pt 2
            valid = True
            
            for num in nums:
                if not valid_nums[int(num)]:
                    count+= int(num)
                    #for pt 2
                    valid = False
            #for pt 2
            if valid:
                valid_tickets.append(nums)
    
    print("part one:",count)
    
    #for pt 2
    #for each range remove the position which it cant be
    for ticket in valid_tickets:
        for i,num in enumerate(ticket):
            for rang in all_ranges:
                if i in all_ranges[rang] and not is_valid(rang,num):
                    all_ranges[rang].remove(i)
    #for each range the only has one option remove that option from all the other ranges
    keep_going = True
    while keep_going:
        keep_going=False
        for range_ in all_ranges:
            if len(all_ranges[range_])==1:
                looking_for = all_ranges[range_][0]
                for range2 in all_ranges:
                    if range2 != range_ and looking_for in all_ranges[range2]:
                        all_ranges[range2].remove(looking_for)
            if len(all_ranges[range_])>1:
                keep_going=True
    
    #count the multiplied sum of all the departered ranges
    count=1
    for rang in all_ranges:
        if "departure" in rang_to_name[rang]:
            count *=  int(my_ticket[all_ranges[rang][0]])
    print("part two:",count)
    
    
def is_valid(ranges,num):
    ranges=re.split("(?:\['|', '|'])",ranges)
    ranges=list(filter(lambda x: (x is not ""),ranges))
            
    for r in ranges:
        r=re.split("-",r)
        if int(num)>=int(r[0]) and int(num)<=int(r[1]):
            return True
    return False


day16()