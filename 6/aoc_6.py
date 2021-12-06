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
    days = 10
    day = 0
    current_fishes = len(fishes)

    while day < days:
        temp_fishes = [] 
        zeros = len([x for x in fishes if x==0])
        #print("ok")
        temp_fishes.append([8]*zeros)
            
        fishes = [x-1 if x != 0 else x for x in fishes ]
        fishes.append(temp_fishes)
        #print(fishes) # print evolution
        day += 1
    return len(fishes)

print("part 1:")
print(part1(example))
print(part1(input))

input = [int(x) for x in open("6/input.txt").read().split(",")]
example = [int(x) for x in open("6/example.txt").read().split(",")]

print("part 2:")
print(part2(example))
