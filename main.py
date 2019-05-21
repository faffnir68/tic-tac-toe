# Créer la tableboard
def board_game(board):
    print('\n'*10)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

table_board = ["#", "X", "O", "X", "X", "O", "X", "X", "O", "X"]
board_game(table_board)
# Créer les joueurs en laissant le premier joueur choisir X ou O

def player_input():
    player1 = input("Player 1: please choose between 'X' or 'O' by typing your choice :").upper()
    if player1 == 'X':
        player2 = 'O'
        return player1, player2
    elif player1 == 'O':
        player2 = 'X'
        return player1, player2
    else:
        player_input()

print(player_input())

def place_marker()

# Implémenter ce que joueur 1 a entré
# Regarder si joueur 1 a gagné ou s'il y égalité
# Passer à joueur 2
# Demander à rejouer