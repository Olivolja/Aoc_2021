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

print(part1(input))