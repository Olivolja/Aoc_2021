import math
input = open("1/input.txt").read().split("\n")
input = [int(x) for x in input]

prev = input[0]

change = 0

for i in input:
    if i > prev:
        change +=1
    prev = i
print(change)


#2
prevsum = input[0] + input[1] + input[2]
change = 0

for i in range(len(input)-2):

    sum = input[i] + input[i+1] + input[i+2]
    if sum > prevsum:
        change +=1
    prevsum = sum

print(change)