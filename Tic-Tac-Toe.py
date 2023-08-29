from IPython.display import clear_output
import random


def display_board(board):
    row1 = slice(1, 4)
    row2 = slice(4, 7)
    row3 = slice(7, 10)
    print(board[row1])
    print(board[row2])
    print(board[row3])


def player_input():
    choices = ['X', 'O']
    while True:
        choice = input('do you want to be "X" or "O"?\n').upper()
        if choice in choices:
            return choice
        else:
            print("wrong entry")


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    if board[1] == board[2] == board[3] == mark or board[4] == board[5] == board[6] == mark or board[7] == board[8] == \
            board[9] == mark or board[1] == board[4] == board[7] == mark or board[2] == board[5] == board[8] == mark or\
            board[3] == board[6] == board[9] == mark or board[1] == board[5] == board[9] == mark or board[3] == board[
            5] == board[7] == mark:
        print(f'{mark} won!')
        return True


def choose_first():
    return f'player {random.randint(1, 2)} goes first'


def space_check(board, position):
    if board[position] != ' ':
        print('space occupied')
        return False
    return True


def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    print("board is full, it's a draw")
    return True


def player_choice(board):
    choices = range(1, 10)
    while True:
        choice = int(input("enter a number between 1-9\n"))
        if not space_check(board, choice):
            continue
        if choice in choices:
            return choice


def replay():
    while True:
        choice = input("do you want to play again? y/n\n").upper()
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False


print('Welcome to Tic Tac Toe!')

default_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
game_on = True
while True:
    display_board(default_board)
    player1 = player_input()
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print(choose_first())

    while game_on:
        # Player1's turn
        clear_output()
        display_board(default_board)
        place_marker(default_board, player1, player_choice(default_board))
        if win_check(default_board, player1) or full_board_check(default_board):
            break

        # Player2's turn.
        clear_output()
        display_board(default_board)
        place_marker(default_board, player2, player_choice(default_board))
        if win_check(default_board, player2) or full_board_check(default_board):
            break

    if not replay():
        break
