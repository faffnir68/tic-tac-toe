#player1 = input("Please pick a marker 'X' or 'O'")
#position = int(input("Please enter a number"))


def display_board(board):
    print('\n' * 100)
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print("-----------")
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')


test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
display_board(test_board)

def player_choose(player_mark_choice):
    pass

def player_play(board, player_position):
    pass

def player_win(board):
    pass