#### connect four

user1 = input("Hello Player 1, welcome to Connect Four! What is your name? > ")
user2 = input("Hello Player 2, welcome to Connect Four! What is your name? > ")
game = 'running'

board = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]

def print_board(board):
    print("Here is the board:")
    print(f"| {board[0][0]} | {board[0][1]} | {board[0][2]} | {board[0][3]} | {board[0][4]} | {board[0][5]} | {board[0][6]} |")
    print("-----------------------------")
    print(f"| {board[1][0]} | {board[1][1]} | {board[1][2]} | {board[1][3]} | {board[1][4]} | {board[1][5]} | {board[1][6]} |")
    print("-----------------------------")
    print(f"| {board[2][0]} | {board[2][1]} | {board[2][2]} | {board[2][3]} | {board[2][4]} | {board[2][5]} | {board[2][6]} |")
    print("-----------------------------")
    print(f"| {board[3][0]} | {board[3][1]} | {board[3][2]} | {board[3][3]} | {board[3][4]} | {board[3][5]} | {board[3][6]} |")
    print("-----------------------------")
    print(f"| {board[4][0]} | {board[4][1]} | {board[4][2]} | {board[4][3]} | {board[4][4]} | {board[4][5]} | {board[4][6]} |")
    print("-----------------------------")
    print(f"| {board[5][0]} | {board[5][1]} | {board[5][2]} | {board[5][3]} | {board[5][4]} | {board[5][5]} | {board[5][6]} |")

def winning_conditions(board):
    #webstite used to help on this portion of code: https://stackoverflow.com/questions/29949169/python-connect-4-check-win-function
    length = len(board[0])
    width = len(board)
    #Horizontal Check for win
    for y in range(length):
        for x in range(width - 3):
            if [x][y] == 'X' and [x + 1][y] == 'X' and [x + 2][y] == 'X' and [x + 3][y] == 'X':
                print(f"Congratiulations {user1}, you won the Game!")
                return True
            elif [x][y] == 'O' and [x + 1][y] == 'O' and [x + 2][y] == 'O' and [x + 3][y] == 'O':
                print(f"Congratulations {user2}, you won the Game!")
                return True
print_board(board)
turn = 0
while game == 'running':
    if turn % 2 == 0.0:
        choice_1_column = int(input("What column would you like to place the X?"))
        run = 'run'
        # Checking to see if they put a number in or a different character, or if they put a number bigger than 7 in.
        while run == 'run':
            if isinstance(choice_1_column, int):
                run = 'not run'
            else:
                print("That is not a number, please try again.")
                choice_1_column = int(input("What column would you like to place the X?"))
                choice_1_column = choice_1_column - 1
        choice_1_column = int(choice_1_column)
        # Checking to see if number is out of range.
        if choice_1_column > 7:
            print("You cannot choose that number, that is too high. Please try again.")
            choice_1_column = int(input("What column would you like to place the X?"))
            choice_1_column = choice_1_column - 1
        else:
            choice_1_column = choice_1_column - 1
        # Checking to see if the column is full.
        if board[0][choice_1_column] == 'X' or board[0][choice_1_column] == 'O':
            print("That column is full, please try again.")
            choice_1_column = int(input('What column would you like to place the X?'))
            choice_1_column = choice_1_column - 1
        # checking to see if the bottom of the board is full, if it is not, then it will place it in the open one.
        if board[5][choice_1_column] == '-':
            board[5][choice_1_column] = 'X'
        elif board[4][choice_1_column] == '-':
            board[4][choice_1_column] = 'X'   
        elif board[3][choice_1_column] == '-':
            board[3][choice_1_column] = 'X'
        elif board[2][choice_1_column] == '-':
            board[2][choice_1_column] = 'X'
        elif board[1][choice_1_column] == '-':
            board[1][choice_1_column] = 'X'
        elif board[0][choice_1_column] == '-':
            board[0][choice_1_column] = 'X'
        elif board[0][choice_1_column] == 'X' or board[0][choice_1_column] == 'O':
            print("That column is full, please try again.")
            choice_1_column = int(input('What column would you like to place the X?'))
            choice_1_column = choice_1_column - 1
        winning_conditions(board)
        if winning_conditions == True:
            break
        else:
            pass
        turn = turn + 1
        print_board(board)
    if turn % 2 == 1.0:
        choice_2_column = int(input("What column would you like to place the O?"))
        run = 'run'
        # Checking to see if they put a number in or a different character, or if they put a number bigger than 7 in.
        while run == 'run':
            if isinstance(choice_1_column, int):
                run = 'not run'
            else:
                print("That is not a number, please try again.")
                choice_1_column = int(input("What column would you like to place the X?"))
                choice_1_column = choice_1_column - 1
        choice_1_column = int(choice_1_column)
        # Checking to see if number is out of range.
        if choice_2_column > 7:
            print("You cannot choose that number, that is too high. Please try again.")
            choice_2_column = int(input("What column would you like to place the O?"))
            choice_2_column = choice_2_column - 1
        else:
            choice_2_column = choice_2_column - 1
        if board[0][choice_2_column] == 'X' or board[0][choice_2_column] == 'O':
            print("That column is full, please try again.")
            choice_2_column = int(input('What column would you like to place the O?'))
            choice_2_column = choice_2_column - 1
        if board[5][choice_2_column] == '-':
            board[5][choice_2_column] = 'O'
        elif board[4][choice_2_column] == '-':
            board[4][choice_2_column] = 'O'   
        elif board[3][choice_2_column] == '-':
            board[3][choice_2_column] = 'O'
        elif board[2][choice_2_column] == '-':
            board[2][choice_2_column] = 'O'
        elif board[1][choice_2_column] == '-':
            board[1][choice_2_column] = 'O'
        elif board[0][choice_2_column] == '-':
            board[0][choice_2_column] = 'O'
        turn = turn + 1
        print_board(board)