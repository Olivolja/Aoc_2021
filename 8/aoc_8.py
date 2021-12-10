import math
import re
input_lines = [x for x in open("8/input.txt").read().split("\n")]
example_lines = [x for x in open("8/example.txt").read().split("\n")]


def part1(lines):
    data = get_outputs(lines)
    sum_of_numbers = 0
    for line in data:
        for elem in line:
            l = len(elem)
            if l == 2 or l == 3 or l == 4 or l == 7:
                sum_of_numbers +=1

    # print(f"sum: {sum_of_numbers}")
    return sum_of_numbers


def part2(lines):
    data = format_data(lines)
    # seg_values = {"a": 8, "b": 6, "c": 8, "d": 7, "e": 4, "f": 9, "g": 7}

    sum_of_numbers = 0

    for display in data:       

        one = display[0][0]     # cf
        four = display[0][2]    # bcdf
        seven = display[0][1]   # acf
        eight = display[0][-1]  # abcdefg

        letter_count = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0}
        for word in display[0]:
            for letter in word:
                letter_count[letter] += 1
        # print(letter_count)
               
        f = [key for key, value in letter_count.items() if value == 9][0] #done
        e = [key for key, value in letter_count.items() if value == 4][0] #done
        b = [key for key, value in letter_count.items() if value == 6][0] #done
        a = [letter for letter in seven if letter not in one][0] #done
        c = [letter for letter in one if letter != f][0]    #done
        d = [letter for letter in four if letter not in seven and letter != b][0] 
        g = [letter for letter in eight if letter != a and letter != b and letter != c and letter != d and letter != e and letter != f ][0] 


        translate =  {a: "a",
                      b: "b",
                      c: "c",
                      d: "d",
                      e: "e",
                      f: "f",
                      g: "g"
                    }
        # print(translate)

        total_number = 0
        for word in display[1]:

            number = 0
            translated_word = ""

            # translate output
            for letter in word:
                translated_word += translate[letter]
            
            translated_word = "".join(sorted(translated_word))
            # print(translated_word)
            # get value from translated word
            if translated_word == "abcefg":
                number = 0
            elif translated_word == "cf":
                number = 1
            elif translated_word == "acdeg":
                number = 2
            elif translated_word == "acdfg":
                number = 3
            elif translated_word == "bcdf":
                number = 4
            elif translated_word == "abdfg":
                number = 5
            elif translated_word == "abdefg":
                number = 6
            elif translated_word == "acf":
                number = 7
            elif translated_word == "abcdefg":
                number = 8
            elif translated_word == "abcdfg":
                number = 9

            total_number *= 10
            total_number += number
        # print(total_number)
        sum_of_numbers += total_number
    # print(sum_of_numbers)
    return sum_of_numbers


def format_data(lines): # output = [[[x1, x2, x3, .. x10], [y1, y2, y3, y4], [[..],[..]]....] SORTED first subarray
    output = lines
    for i, line in enumerate(lines):
        data_i = line
        data_i = re.split(" ", line)
        output[i] = [sorted(data_i[0:10], key=len), data_i[11:]]
    return output #remove [0] this is for testing


def get_outputs(lines):
    output = lines
    for i, line in enumerate(lines):
        data_i = line
        data_i = re.split(" ", line)
        output[i] = sorted(data_i[11:], key=len)
    return output 


print(f"Example Part 1: {part1(example_lines)}")
print(f"Part 1: {part1(input_lines)}")
print("")
#reset data
input_lines = [x for x in open("8/input.txt").read().split("\n")]
example_lines = [x for x in open("8/example.txt").read().split("\n")]
print(f"Part 2: {part2(input_lines)}")