import math
input = open("4/input.txt").read().split("\n")
def part1(input):
    draws = input[0].split(",")
    del input[:2] #input is now "" ,lines in board, ""
    boards = generate_boards(input)
    for number in draws:
        for board_i in range(len(boards)):
            for row in range(len(boards[board_i])):
                for e in range(len(boards[board_i][row])):
                    #check number and replase with x if exist
                    if boards[board_i][row][e] == number:
                        boards[board_i][row][e]  = "x"
                    else:
                        continue
                    #check if winner exist
                    winning_table = check_win(boards)
                    if(winning_table):
                        return sum_board(boards[winning_table]) * int(number)
    return False

def sum_board(board):
    sum = 0
    for row_i, row in enumerate(board):
        for e_i, e in enumerate (row):
            if (e != "x"):
                sum += int(e)
    return sum

def generate_boards(boardlines):
    boards = []
    currentboard = []
    for line in input:
        if(line ==""):
            boards.append(currentboard)
            currentboard = []
        else:
            l = line.split(" ")
            l = [x for x in l if x!=""]
            currentboard.append(l)
    return boards

def check_win(boards):
    winning_table = False

    for table_index, table in enumerate(boards):
        for row_i, row in enumerate(table):
            if row == ["x", "x", "x", "x", "x"]:
                winning_table = table_index

    for table_index, table in enumerate(boards):
        trasnposed_table = list(map(list, zip(*table)))
        for row_i, row in enumerate(trasnposed_table):
            if row == ["x", "x", "x", "x", "x"]:
                winning_table = table_index
    return winning_table

def check_wins(boards):
    winning_tables = set([])

    for table_index, table in enumerate(boards):
        for row_i, row in enumerate(table):
            if row == ["x", "x", "x", "x", "x"]:
                winning_tables.add(table_index)

    for table_index, table in enumerate(boards):
        trasnposed_table = list(map(list, zip(*table)))
        for row_i, row in enumerate(trasnposed_table):
            if row == ["x", "x", "x", "x", "x"]:
                winning_tables.add(table_index)
    return winning_tables

def part2(input):
    draws = input[0].split(",")
    del input[:2] #input is now "" ,lines in board, ""
    boards = generate_boards(input)
    for number in draws:
        for board_i in range(len(boards)):
            for row in range(len(boards[board_i])):
                for e in range(len(boards[board_i][row])):
                    #check number and replase with x if exist
                    if boards[board_i][row][e] == number:
                        boards[board_i][row][e]  = "x"
                    else:
                        continue
                    #check if winners
                    wins = check_wins(boards)
                    if(len(wins) == len(boards)-1):
                        left = set(range(0,98)) - wins
                    if(len(wins) == len(boards)):
                        return sum_board(boards[left.pop()]) * int(number)
    return False

print(f"Part 1: {part1(input)}")      
input = open("4/input.txt").read().split("\n")
print(f"Part 2: {part2(input)}")