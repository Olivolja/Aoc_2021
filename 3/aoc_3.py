import math
input = open("3/input.txt").read().split("\n")
example = open("3/example.txt").read().split("\n")
hax = open("3/hax.txt").read().split("\n")

#input = [x.split(" ") for x in input]



def part1(list):
    gamma = []
    epsilon = []
    
    for i in range(len(list[0])):
        ones = 0
        zeros = 0
        for row in list:
            if int(row[i]) == 1:
                ones +=1
            else:
                zeros +=1
        most = 1 if ones > zeros else 0
        least = 0 if ones > zeros else 1
        gamma.append(most)
        epsilon.append(least)
   
    g = int("".join(map(str,gamma)),2)
    e = int("".join(map(str,epsilon)),2)
    # print(gamma,epsilon)
    # g = 0
    # e = 0
    # gamma.reverse()
    # epsilon.reverse()
    # for i in range(len(gamma)):
    #     g += gamma[i] * (2**i)
    #     e += epsilon[i]*(2**i)
    # print(int(t,2) * int(y,2))

    return g*e



def part2(list):
    oxygen = 0
    co2 = 0

    oxygen_list = [x for x in list]
    co2_list = [x for x in list]
    
    for i in range(len(list[0])):        
        ox_ones = 0
        ox_zeros = 0
        co2_ones = 0
        co2_zeros = 0

        for row in oxygen_list:
            if int(row[i]) == 1:
                ox_ones +=1
            else:
                ox_zeros +=1
        for row in co2_list:
            if int(row[i]) == 1:
                co2_ones +=1
            else:
                co2_zeros +=1
        most = 1 if ox_ones >= ox_zeros else 0
        least = 0 if co2_ones >= co2_zeros else 1
        #filter 
        if(len(oxygen_list) != 1):
            oxygen_list = [x for x in oxygen_list if int(x[i])==most]
        if(len(co2_list) != 1):
            co2_list = [x for x in co2_list if int(x[i])==least]
        if (len(co2_list) == 1 and len(oxygen_list) == 1):
            break

    #reverse string

    oxygen = int("".join(oxygen_list),2)
    co2 = int("".join(co2_list),2)

    
    return(oxygen * co2)

print(f"mine part 1: {part1(input)}")
print(f"hax part 1: {part1(hax)}")
print(f"mine part 2: {part2(input)}")
print(f"example part 2: {part2(example)}")