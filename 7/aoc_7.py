import math
import re
input = [int(x) for x in open("7/input.txt").read().split(",")]
example = [int(x) for x in open("7/example.txt").read().split(",")]

print(input[0])
def part1(crabs):
    minfuel = 1000000
    for pos in range(min(crabs), max(crabs),1):
        fuel = 0
        for crab in crabs:
            fuel += abs(pos-crab)
        if fuel < minfuel:
            minfuel = fuel  
    return minfuel

# def part2(crabs):
#     minfuel = 100000000000000
#     for pos in range(min(crabs), max(crabs),1):
#         fuel = 0
#         for crab in crabs:
#             fuel += helpcrab_calculate_fuel(crab, 1, pos)
#         if fuel < minfuel:
#             minfuel = fuel  
#     return minfuel

# def helpcrab_calculate_fuel(crab, fuel_per_step, destination):
#     if crab == destination:
#         return fuel_per_step
#     next_step_fuel = fuel_per_step + 1
#     if destination > crab:
#         crab += 1
#     else:
#         crab += 1
    
def part2(crabs):
    minfuel = 100000000000
    for pos in range(min(crabs), max(crabs),1):
        fuel = 0
        crab_dist_to_pos = [abs(pos - crab) for crab in crabs]
        for dist in crab_dist_to_pos:
            fuel += (dist*(dist + 1)) // 2
            # print(fuel)
        if fuel < minfuel:
            minfuel = fuel  
    return minfuel

    return fuel_per_step + helpcrab_calculate_fuel(crab, next_step_fuel, destination)

print(f"Part 1: {part1(input)}")

print(f"Part 2: {part2(input)}")