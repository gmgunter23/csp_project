#### connect four

from secrets import choice


user1 = input("Hello Player 1, welcome to Connect Four! What is your name? > ")
user2 = input("Hello Player 2, welcome to Connect Four! What is your name? > ")
game = 'running'


board = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]

def print_board(board):
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

print("Here is the board:")
print_board(board)
count = 0

while game == 'running':
    if count % 2 == 0.0:
        choice_1_column = int(input("What column would you like to place the X?"))
        board[choice_1_column] = 'X'
        count = count + 1
        print_board(board)
    if count % 2 == 1.0:
        choice_2_column = int(input("What column would you like to place the O?"))
        board[choice_2_column] = 'O'
        count = count + 1
        print_board(board)

