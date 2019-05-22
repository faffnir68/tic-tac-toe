# Créer la tableboard
def board_game(board):
    print('\n'*10)
    print('   |   |')
    print('  ' + board[7] + ' | ' + board[8] + '  | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print('  ' + board[1] + ' | ' + board[2] + '  | ' + board[3])
    print('   |   |')

# Créer les joueurs en laissant le premier joueur choisir X ou O
def player_input():
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'

# Enter a position for the mark

def place_marker(board, marker, position):
    board[position] = marker

# Check if a player has won
def has_won(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[1] == mark and board[4] == mark and board[7] == mark) or
            (board[2] == mark and board[5] == mark and board[8] == mark) or
            (board[3] == mark and board[6] == mark and board[9] == mark) or
            (board[1] == mark and board[5] == mark and board[9] == mark) or
            (board[3] == mark and board[5] == mark and board[7] == mark)
            )

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Type the position you want the mark in (1-9): "))
    return position

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

# Start the app
print("Welcome to Tic Tac Toe")
while True:
    the_board = ['#', '', '', '', '', '', '', '', '', '']
    player1_marker, player2_marker = player_input()
    board_position = int(input("Type the position you want the mark in (1-9): "))
    place_marker(the_board, player1_marker, board_position)
    print(board_game(the_board))

