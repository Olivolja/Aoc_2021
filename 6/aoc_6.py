import math
import re
input = [int(x) for x in open("6/input.txt").read().split(",")]
example = [int(x) for x in open("6/example.txt").read().split(",")]
#print(len(input))
print([8]*10)
def part1(input):
    fishes = input #clone list cuz idk
    days = 80
    day = 0
    current_fishes = len(fishes)
    while day < days:
        for fish_i in range(current_fishes):
            #decrease day

            if fishes[fish_i] <= 0:
                #make new fish and set its day to 8 and this fish to 6
                fishes[fish_i] = 6
                fishes.append(8)
            else:
                fishes[fish_i] -= 1
            current_fishes = len(fishes)
        #print(fishes) # print evolution
        day += 1
    return len(fishes)

def part2(input):
    fishes = input #clone list cuz idk
    days = 256 
    sum = 0
    for f in fishes:
        sum += fish(f, days)
    return sum

def fish(me, days):
    children = 0
    if days == 0:
        return 1
    if(me <= 0):
        me = 6
        children += fish(8, days-1)
    else:
        me -= 1

    return fish(me, days-1) + children


print("part 1:")
print(part1(example))
print(part1(input))

input = [int(x) for x in open("6/input.txt").read().split(",")]
example = [int(x) for x in open("6/example.txt").read().split(",")]

print("part 2:")
print(part2(input))
