import copy

def check_board(board):
    check_list = [-1, -1, -1, -1, -1]
    for row in range(0, len(board),1):
        if board[row] == check_list:
            return True
        for col in range(0, len(board[row]), 1):
            check = list(map(lambda x: x[col],board))
            if check == check_list:
                return True
    return False

with open('data/puzzle_four.txt') as f:
    lines = list(map(lambda l: l.replace('  ', ' ').strip(),
                     list(filter(lambda x: x != "",
                                 list(map(lambda x: x.replace("\n", ""), f.readlines()))))))

    winning_numbers = lines[0].split(',')
    boards = lines[1:]
    boards_string_list = list(map(
        lambda x: list(map(
            lambda p: p.split(' '), boards[x:x+5]))
        , range(0, len(boards), 5)))
    board_ix = -1

    temp_boards = copy.deepcopy(boards_string_list)
    found = False
    winning_num = -1
    list_of_won_boards = list()
    t = None
    counter = 0
    for check_num in winning_numbers:
        for i in range(0, len(temp_boards), 1):
            if i in list_of_won_boards:
                continue
            for row in range(0, len(temp_boards[i]), 1):
                for col in range(0, len(temp_boards[i][row]), 1):
                    if temp_boards[i][row][col] == check_num:
                        temp_boards[i][row][col] = -1
            if check_board(temp_boards[i]):
                list_of_won_boards.append(i)
                t = (temp_boards[i], check_num)
                if len(list_of_won_boards) > 99:
                    break
    print(counter)


    sum = 0
    for el in temp_boards[board_ix]:
        for p in el:
            if p != -1:
                sum += int(p)
    print(sum * winning_num)



