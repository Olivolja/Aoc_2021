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

def part1_recursive(input):
    fishes = input #clone list cuz idk
    days = 80 
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

# This part is heavily inspired by https://github.com/flippeman
def part2(input):
    school = [0]*7
    gingergarden = [0,0]
    days = 256
    for fish in input:
        school[fish] += 1
    for i in range(0, days, 1):
        new_fish = school[i%7]
        school[i%7] += gingergarden.pop(0)
        gingergarden.append(new_fish)
        new_fish = 0
    return sum(school) + sum(gingergarden)


print("part 1:")
print(part1(example))
print(part1(input))

input = [int(x) for x in open("6/input.txt").read().split(",")]
example = [int(x) for x in open("6/example.txt").read().split(",")]

print("part 2:")
print(part2(input))
