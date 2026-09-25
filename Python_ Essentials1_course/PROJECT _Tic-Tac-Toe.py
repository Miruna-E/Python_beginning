# a simple program which pretends to play tic-tac-toe with the user
# computer with X, user with O

# requirements
# board should be stored as a three-element list, while each element(a row) is another three-element list 
# square = board[row][column] = 'O', 'X' or digit for the square's number (free square)
# the board's appearance should be exactly the same as the one presented in the example.

global board_size
board_size = 3
global max_board_square_nr
max_board_square_nr = board_size * board_size

def display_board(board):
    """
    The function accepts one parameter containing the board's current status
    and prints it out to the console.
    """

    print("+-------+-------+-------+")
    for row in range(board_size):
        print("|       |       |       |")
        print("|   ", end="")
        for column in range(board_size):
            print(board[row][column], end="   |   ")
        print("", end="\n")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def make_list_of_free_fields(board):
    """
    The function browses the board and builds a list of all the free squares; 
    the list consists of tuples, while each tuple is a pair of row and column numbers.
    """

    free_fields = []
    for row in range(board_size):
        for column in range(board_size):
            if(board[row][column] not in ['X', 'O']):
                free_fields.append((row, column))

    return free_fields

def enter_move(board):
    """
    The function accepts the board's current status, asks the user about their move, 
    checks the input, and updates the board according to the user's decision.
    """
    
    while(True):
        try:
            move = int(input("Enter your move: ")) # the number of the square they choose
            if(move > 0 and move <= max_board_square_nr):
                row = (move - 1) // board_size
                column = (move - 1) % board_size

                if(board[row][column] in ['X', 'O']):
                    print("Field is already occupied")
                else:
                    board[row][column] = 'O'
                    break
            else:
                print("A move must be a number, greater than 0, less than", max_board_square_nr + 1)
        except:
            print("A move must be a number, greater than 0, less than", max_board_square_nr + 1)

def draw_move(board):
    """
    The function draws the computer's move and updates the board.
    """

    from random import randrange

    free_fields = make_list_of_free_fields(board)
    free_fields_count = len(free_fields)
    if(free_fields_count == 0):
        print("No free fields left!")
        return

    move = randrange(free_fields_count)
    row, column = free_fields[move]
    board[row][column] = 'X'

def victory_for(board, sign):
    """
    The function analyzes the board's status in order to check if 
    the player using 'O's or 'X's has won the game

    four possible verdicts: 
    1. the game should continue
    2. the game ends with a tie
    3. you win
    4. computer wins
    """

    if(sign == 'X'):
        winner = "calculator"
    elif(sign == 'O'):
        winner = "player"
    else:
        victory_for(board, input("Wrong sign entered! Enter an X or a O"))

    second_diagonal = first_diagonal = 1
    for i in range(3):
        if(board[i][0] == sign and board[i][1] == sign and board[i][2] == sign):
            return winner
        elif(board[0][i] == sign and board[1][i] == sign and board[2][i] == sign):
            return winner
        if(board[i][i] != sign):
            first_diagonal = 0
        if(board[2 - i][2-i] != sign):
            second_diagonal = 0

    if(first_diagonal or second_diagonal):
        return winner
    return None

    # # TO DO: working on making this work for all board sizes
    # impossible_rows = [0] * board_size
    # impossible_collumns = [0] * board_size
    # good_quares = [] # list of (row, column,) tuples of squares that can indicate that someone has won
    # crt_row = 0
    # crt_column = 0

    # while(crt_row + 1 < board_size and crt_column + 1 < board_size):
    #     if(board[crt_row][crt_column] != sign): #current box is not the sign we are looking for
    #         impossible_rows[crt_row] = 1
    #         impossible_collumns[crt_column] = 1
    #         crt_row += 1
    #         crt_column += 1
    #     else: 
    #         good_square = 1

    #         if(board[crt_row + 1][crt_column] != sign): #neighbor downwards is the wrong sign
    #             impossible_collumns[crt_column] = 1
    #             crt_column += 1
    #             good_square = 0

    #         if(board[crt_row][crt_column + 1] != sign): #neighbor on the right is the wrong sign
    #             impossible_rows[crt_row] = 1
    #             crt_row += 1
    #             good_square = 0

    #         if(board[crt_row + 1][crt_column + 1] != sign): #neighbor on the second diagonal is the wrong sign
    #             second_diagonal = 0
    #             good_square = 0

    #         if(good_square):
    #             good_quares.append((crt_row, crt_column,))

    # if(second_diagonal or first_diagonal):
    #     return winner
    # else:
    #     return None

    
board = []

# all the squares are numbered row by row starting with 1
square_nr = 1
for row_index in range(board_size):
    crt_row = []
    for column_index in range(board_size):
        crt_row.append(square_nr)
        square_nr += 1

    board.append(crt_row)

board[1][1] = 'X' # first move: computer puts X in the middle
player_turn = 1
display_board(board)

game_ongoing = 1
while(game_ongoing):

    if(player_turn):
        enter_move(board)
        if(victory_for(board, 'O')):
            print("You won")
            game_ongoing = 0
        player_turn = 0
    else:
        draw_move(board)
        if(victory_for(board, 'X')):
            print("You lost")
            game_ongoing = 0
        player_turn = 1

    display_board(board)

    if(game_ongoing and len(make_list_of_free_fields(board)) == 0):
        print("It's a tie")
        game_ongoing = 0
        break