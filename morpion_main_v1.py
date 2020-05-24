# jeu de morpion, projet de TSTI2D

from random import shuffle, random


def display_board(board):
    for i in range(0, 9, 3):
        print('|{}|{}|{}|'.format(board[i], board[i + 1], board[i + 2]))


def check_spot_taken(board, spot):
    return not board[spot].isdigit()


def check_win(board, symbol):
    return ((board[0] == symbol and board[1] == symbol and board[2] == symbol) or
            (board[3] == symbol and board[4] == symbol and board[5] == symbol) or
            (board[6] == symbol and board[7] == symbol and board[8] == symbol) or
            (board[0] == symbol and board[3] == symbol and board[6] == symbol) or
            (board[1] == symbol and board[4] == symbol and board[7] == symbol) or
            (board[2] == symbol and board[5] == symbol and board[8] == symbol) or
            (board[0] == symbol and board[4] == symbol and board[8] == symbol) or
            (board[2] == symbol and board[4] == symbol and board[6] == symbol))


def check_full(board):
    string = ''
    for i in range(9):
        string += board[i]
    return string.isalpha()


def computer_strategy(board):
    possible_moves = [x for x, content in enumerate(board) if content.isdigit()]
    board_test = board.copy()
    chosen_move = 9

    # if possible win, win or if player can win, block
    for symbol_test in ['O', 'X']:
        for i in possible_moves:
            board_test[i] = symbol_test
            # print(board_test)
            if check_win(board_test, symbol_test):
                chosen_move = i
                break
            board_test[i] = str(i + 1)

    # else chose center
    if 4 in possible_moves and chosen_move == 9:
        chosen_move = 4
    elif chosen_move == 9:
        shuffle(possible_moves)
        chosen_move = possible_moves.pop()

    return chosen_move


def two_players_game():
    board = [str(i) for i in range(1, 10)]
    play_again = True

    while play_again:
        for i in range(1, 3):
            display_board(board)

            if i == 1:
                symbol = 'X'
            else:
                symbol = 'O'

            spot_taken = True
            while spot_taken:
                question = 'Joueur ' + str(i) + ', où voulez-vous jouer ? '
                spot = int(input(question)) - 1
                if check_spot_taken(board, spot):
                    print('Attention case déjà prise...')
                else:
                    spot_taken = False

            board[spot] = symbol

            if check_win(board, symbol):
                display_board(board)
                print('C\'est gagné joueur', i, '!')
                play_again = False
                break

            elif check_full(board):
                print('Match nul !')
                play_again = False
                break


def one_player_game():
    board = [str(i) for i in range(1, 10)]
    play_again = True

    while play_again:
        for i in range(1, 3):
            if i == 1:
                symbol = 'X'
                display_board(board)
                spot_taken = True
                while spot_taken:
                    question = 'Où voulez-vous jouer ? '
                    spot = int(input(question)) - 1
                    if check_spot_taken(board, spot):
                        print('Attention case déjà prise...')
                    else:
                        spot_taken = False
            else:
                symbol = 'O'
                spot = computer_strategy(board)

            board[spot] = symbol

            if check_win(board, symbol):
                display_board(board)
                if symbol == 'X':
                    print('C\'est gagné !')
                else:
                    print('Vous avez perdu.')
                play_again = False
                break

            elif check_full(board):
                print('Match nul !')
                play_again = False
                break


def menu():
    print('Bienvenue dans le jeu de morpion !')
    repeat = True
    while repeat:
        choice = input('Quel mode de jeu souhaitez-vous ?\n1 : deux joueurs, 2 : contre l\'ordinateur... ')
        if choice == 1:
            two_players_game()
        else:
            one_player_game()
        choice2 = input('Voulez-vous rejouer ? (oui/non) ')
        if choice2.lower() == 'non':
            repeat = False
    print('Bye...')


if __name__ == "__main__":
    menu()
