def field_output(): # Console output function
    field = [[' ', ' ',        '0',        ' ',        '1',        ' ',          '2',      ' '], \
             ['0', '|', field_input[0][0], '|', field_input[0][1], '|', field_input[0][2], '|'], \
             ['1', '|', field_input[1][0], '|', field_input[1][1], '|', field_input[1][2], '|'], \
             ['2', '|', field_input[2][0], '|', field_input[2][1], '|', field_input[2][2], '|']]
    for i in field:
        print(*i)
        print('    -   -   -  ')

def player_move_and_checking(): # The function enters the x,y coordinates and checks the correctness of the values
    while True:
        print(f'Player', player)
        x = input('Enter the X coordinate  = ')            # input x
        y = input('Enter the Y coordinate  = ')            # input y
        if x in ['0', '1', '2'] and y in ['0', '1', '2']:  # checking the values x и y
            if field_input[int(x)][int(y)] != ' ':         # check that the cell is free
                print('The field is occupied')             # please re-enter x and y
            else:
                field_input[int(x)][int(y)] = player       # recording the player's move
                break
        else:
            print('Enter a value from 0 to 2')             # please re-enter x and y

def checking_the_winner(): # Checking the move for a win
    return field_input[0] == [player, player, player] or field_input[1] == [player, player, player] or field_input[2] == [player, player, player] or \
            field_input[0][0] == player and field_input[1][0] == player and field_input[2][0] == player or \
            field_input[0][1] == player and field_input[1][1] == player and field_input[2][1] == player or \
            field_input[0][2] == player and field_input[1][2] == player and field_input[2][2] == player or \
            field_input[0][0] == player and field_input[1][1] == player and field_input[2][2] == player or \
            field_input[0][2] == player and field_input[1][1] == player and field_input[2][0] == player


def player_assignment(): # changing the player
    if count % 2 == 1:
        return 'X' # the first player
    else:
        return '0' # the second player

def banner(): # banner output to the console
    print('The game "Tic-Tac-toe"')

player = 'X'                                  # the first player
count = 0                                     # move counter
field_input = [[' '] * 3 for i in range(3)]   # setting the initial value of the field variable
while True:                                   # the main cycle of the game
    banner()                                  # banner output
    field_output()                            # output the field
    if checking_the_winner():                 # Checking the move for a win
        field_output()                        # output of the field before the announcement of the winner
        print(f'Player', player, 'winner!!!')
        break
    elif count == 9:                          # checking for a draw
        print('Drawn game!!!')
        break
    else:
        count += 1                            # counting moves
        player = player_assignment()          # player assignment
    player_move_and_checking()                # entering and checking player moves




