'''
ProjectEngeto_02.py: The second project to Engeto Online Python Academy

Author: Tomáš Zvardoň
Email: zvardont@seznam.cz
Discord: Tomáš Z.#3385
'''

all_position = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
blank_field = " "


def game_fields() -> dict:
    '''
    Create a new dictionary from list of strings (position on the game
    board as a key), which are associated with blank fields as default
    values.

    :return:
        The dictionary, which represents marks on the game board.
    '''
    fields = {position: blank_field for position in all_position}
    return fields


def game_board(fields: dict) -> str:
    '''
    Create a game board from dictionary values.

    :param fields:
            A dictionary, which represents positions on the
            game board and stored values (blank field as a default
            value). Values are modified by each player's move.

    :return:
            String overview of the actual game board after each player's
            move.
    '''
    f = fields
    return f'''
    +---+---+---+   +---+---+---+                                 
    | {f["1"]} | {f["2"]} | {f["3"]} |   | 1 | 2 | 3 |  
    +---+---+---+   +---+---+---+                                 
    | {f["4"]} | {f["5"]} | {f["6"]} |   | 4 | 5 | 6 |   
    +---+---+---+   +---+---+---+                                 
    | {f["7"]} | {f["8"]} | {f["9"]} |   | 7 | 8 | 9 |   
    +---+---+---+   +---+---+---+                                
    '''


def valid_move(fields: dict, player_move: str) -> bool:
    '''
    Check if player's move is valid.

    :param fields:
            A dictionary, which represents positions on the
            game board and stored values (blank field as a default
            value). Values are modified by each player's move.

    :param player_move:
            Player's move is represented by player's input value.
            Only string digit values, which are put on blank fields,
            are allowed.

    :return:
            True -> player's move is valid.
            False -> player's move is not valid.
    '''
    return player_move in all_position and fields[player_move] == blank_field


def update_game_fields(fields: dict, player_move: str, player_mark: str):
    '''
    Update the player's move into the dictionary values by specific
    player's mark.

    :param fields:
            A dictionary, which represents positions on the
            game board and stored values (blank field as a default
            value). Values are modified by each player's move.

    :param player_move:
            Player's move is represented by player's input value.
            Only string digit values, which are put on blank fields,
            are allowed.

    :param player_mark:
            Player's mark is a specific symbol, which represents
            player's move on the game board.
    '''

    fields[player_move] = player_mark


def check_winner(fields: dict, player_mark: str) -> bool:
    '''
    Check if any player has won, i.e. has created the winning
    combination of the three same player's mark horizontally,
    vertically or diagonally.

    :param fields:
            A dictionary, which represents positions on the
            game board and stored values (blank field as a default
            value). Values are modified by each player's move.

    :param player_mark:
            Player's mark is a specific symbol, which represents
            player's move on the game board.

    :return:
            True -> player has won. Game over.
            False -> player has not won.
    '''
    f, pm = fields, player_mark
    return ((f['1'] == f['2'] == f['3'] == pm) or  # horizontal top
            (f['4'] == f['5'] == f['6'] == pm) or  # horizontal middle
            (f['7'] == f['8'] == f['9'] == pm) or  # horizontal bottom
            (f['1'] == f['4'] == f['7'] == pm) or  # vertical left
            (f['2'] == f['5'] == f['8'] == pm) or  # vertical middle
            (f['3'] == f['5'] == f['9'] == pm) or  # vertical right
            (f['1'] == f['5'] == f['9'] == pm) or  # diagonal \
            (f['3'] == f['5'] == f['7'] == pm))    # diagonal /


def check_tie(fields: dict) -> bool:
    '''
    Check if the game has finished with a tie.

    :param fields:
            A dictionary, which represents positions on the
            game board and stored values (blank field as a default
            value). Values are modified by each player's move.

    :return:
            True -> game is a tie. Game over.
            False -> game is not a tie.
    '''
    for player_move in all_position:
        if fields[player_move] == blank_field:
            return False
    return True


def game_run():
    print('''
    Welcome to Tic Tac Toe game
    ========================================
    GAME RULES:
    Each player can place one mark (or stone)
    per turn on the 3x3 grid. The WINNER is
    who succeeds in placing three of their
    marks in a:
    * horizontal,
    * vertical or
    * diagonal row.
    ========================================
    Let's start the game
    ----------------------------------------''')

    double_separator = "=" * 47
    gf = game_fields()
    first_player, second_player = "X", "O"  # Players' mark.

    while True:  # Main game loop.
        print(game_board(gf))
        move = None
        while not valid_move(gf, move):  # Asking player until entering valid move.
            print(double_separator)
            move = input(f"Player '{first_player}' | Please, enter your move number: ")
            print(double_separator)
            if not move.isnumeric():  # Warning if player's move is not number.
                print("Non numeric inputs not allowed! Try again!")
                continue
            elif move.isnumeric() and move not in all_position:  # Warning if player's move is not number 1 to 9.
                print("Enter only numbers 1 to 9!")
                continue
            elif gf[move] != blank_field:  # Warning if player's move is put on occupied game field.
                print("Selected field is not empty, try another one!")
                continue
        update_game_fields(gf, move, first_player)  # Updating game field with player's move.

        if check_winner(gf, first_player):  # Checking if player has won. Game over.
            print(game_board(gf))
            print(f"Congratulations, player '{first_player}' has won!")
            break
        elif check_tie(gf):  # Checking if game is a tie. Game over.
            print(game_board(gf))
            print(f"The game is a tie!")
            break
        first_player, second_player = second_player, first_player  # Switching turn to the next player.
    print("Game over!")


if __name__ == '__main__':
    game_run()
