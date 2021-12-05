import math
import re
input = open("5/input.txt").read().split("\n")
example = open("5/example.txt").read().split("\n")

def part1(input):
    pair_of_pairs = format_input(input)
    world = [[0]*1000 for x in range(1000)]

    for ppair in pair_of_pairs:
        xmin = min(ppair[0],ppair[2])
        xmax = max(ppair[0],ppair[2])
        ymin = min(ppair[1],ppair[3])
        ymax = max(ppair[1],ppair[3])
        

        if xmin == xmax:
            for y in range(ymin, ymax+1):
                    world[y][xmin] += 1
        if ymin == ymax:
            for x in range(xmin, xmax+1):

                    world[ymin][x] += 1


                
    sum_of_overlap = 0
    for y_row in world:
        for pos in y_row:
            if int(pos) >= 2:
                sum_of_overlap +=1

    return sum_of_overlap
    # return world
    pass


def part2(input):
    #prop not needed later just for me to find out stuff
    pair_of_pairs = format_input(input)

    xs = [[x[0], x[2]] for x in pair_of_pairs]
    xs = [item for sublist in xs for item in sublist]
    ys = [[x[1], x[3]] for x in pair_of_pairs]
    ys = [item for sublist in ys for item in sublist]
    maxx = max(xs)
    maxy = max(ys)
    world = [[0]*(maxx+1) for x in range(maxy+1)]
    pair_of_pairs = format_input(input)

    for ppair in pair_of_pairs:
            xmin = min(ppair[0],ppair[2])
            xmax = max(ppair[0],ppair[2])
            ymin = min(ppair[1],ppair[3])
            ymax = max(ppair[1],ppair[3])
            dir = (ppair[0]-ppair[2], ppair[1]-ppair[3]) 

            if(xmax - xmin == ymax -ymin): #diagonal
                dir = (dir[0]//abs(dir[0]), dir[1]//abs(dir[1]))
                last = (ppair[0], ppair[1])
                current = (ppair[2], ppair[3])
                while current != last:
                    world[current[1]][current[0]] += 1
                    current = (current[0]+ dir[0], current[1] + dir[1])
                world[current[1]][current[0]] += 1
            elif xmin == xmax: #horizontal
                for y in range(ymin, ymax+1):
                    world[y][xmin] += 1
            elif ymin == ymax: #vertical
                for x in range(xmin, xmax+1):
                    world[ymin][x] += 1
       
    sum_of_overlap = 0
    for y_row in world:
        for pos in y_row:
            if int(pos) >= 2:
                sum_of_overlap +=1

    for row in world:
        for cell in row:
            c = "." if cell == 0 else cell
            print(c, end=" ")
        print()

    return sum_of_overlap
    



def format_input(text_lines): # pair of pairs = [[x1,y1,x2,y2],[...]] in strings
    pair_of_pairs = []
    for line in text_lines:
        pair_of_pairs.append(list(map(int,re.split(",| -> ", line))))
    return pair_of_pairs




print(f"part 1: {part1(input)}")

print(f"part 2: {part2(input)}")

print(f"part 2 Example: {part2(example)}")