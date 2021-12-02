import math
input = open("2/input.txt").read().split("\n")
input = [x.split(" ") for x in input]


def part1(commands):
    
    hor = 0
    dep = 0
    for command, amount in commands:
        amount = int(amount)
        if(command == "forward"):
            hor += amount
        elif(command == "down"):
            dep +=amount
        elif(command == "up"):
            dep -=amount
            if(dep < 0):
                dep = 0

    return(hor*dep)


def part2(commands):
    
    hor = 0
    dep = 0
    aim = 0
    for command, amount in commands:
        amount = int(amount)
        if(command == "forward"):
            hor += amount
            dep += aim*amount
        elif(command == "down"):
            aim +=amount
        elif(command == "up"):
            aim -=amount
            if(dep < 0):
                dep = 0

    return(hor*dep)



print(part1(input))
print(part2(input))