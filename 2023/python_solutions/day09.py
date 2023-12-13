def get_last_numbers(nums):
    while any(nums):
        yield nums[-1]
        nums = [b - a for a, b in zip(nums, nums[1:])]


for part in [1, -1]:
    with open("../inputs/day09.txt") as file:
        print(sum(
            sum(get_last_numbers([int(x) for x in line.split()][::part]))
            for line in file
        ))
