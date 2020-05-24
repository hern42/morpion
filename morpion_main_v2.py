# jeu de morpion, projet de TSTI2D

from random import shuffle, random


def display_board(board):
    print('-' * 7)
    for i in range(0, 9, 3):
        print('|{}|{}|{}|'.format(board[i], board[i + 1], board[i + 2]))
    print('-' * 7)


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


def computer_strategy(who, board):
    possible_moves = [x for x, content in enumerate(board) if content.isdigit()]
    board_test = board.copy()
    chosen_move = 42

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
    if 4 in possible_moves and chosen_move == 42:
        chosen_move = 4
    elif chosen_move == 42:
        shuffle(possible_moves)
        chosen_move = possible_moves.pop()

    return chosen_move


def player_move(who, board):
    spot_taken = True

    while spot_taken:
        question = 'Joueur ' + str(who) + ', où voulez-vous jouer ? '
        chosen_move = int(input(question)) - 1
        if check_spot_taken(board, chosen_move):
            print('Attention case déjà prise...')
        else:
            spot_taken = False

    return chosen_move


def game(turn):
    board = [str(i) for i in range(1, 10)]
    symbol = ('X', 'O')
    play_again = True

    while play_again:
        for i in range(1, 3):
            display_board(board)
            spot = turn[i - 1](i, board)
            board[spot] = symbol[i - 1]

            if check_win(board, symbol[i - 1]):
                display_board(board)
                print('C\'est gagné joueur', i, '!')
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
        question = 'Quel mode de jeu souhaitez-vous ?\n1 : deux joueurs, 2 : contre l\'ordinateur, 3 : ordinateur ' \
                   'contre lui même. '
        choice = int(input(question))
        if choice == 1:
            turn = (player_move, player_move)
            game(turn)
        elif choice == 2:
            if random() <= 0.5:
                turn = (player_move, computer_strategy)
            else:
                turn = (computer_strategy, player_move)
            game(turn)
        elif choice == 3:
            turn = (computer_strategy, computer_strategy)
            game(turn)
        else:
            print('Choix invalide...')

        choice2 = input('Voulez-vous rejouer ? (oui/non) ')
        if choice2.lower() == 'non':
            repeat = False
    print('Bye...')


if __name__ == "__main__":
    menu()
