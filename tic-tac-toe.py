from random import randrange

COMPUTER="X"
USER="O"

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for row in board:
        for col_val in row:
            print(col_val, end=" ")
        print()

def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    valid=0
    free_fields=make_list_of_free_fields(board)
    while(valid==0):
        field=int(input("Which field do you want to play: "))
        field=((field-1)//3, (field-1)%3)
        if(field not in free_fields):
            print("Field already filled, please try with other empty fields.. ")
            display_board(board)
            continue
        else:
            board[field[0]][field[1]]=USER
            print("Current status: ")
            display_board(board)
            valid=1

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_fields=list()
    for row in range(len(board)):
        for col_index in range(len(board[0])):
            if(board[row][col_index] != COMPUTER and board[row][col_index] != USER):
                free_fields.append((row, col_index))
    return free_fields

def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    for row_index in range(len(board)):
        if(board[row_index][0] == sign and board[row_index][1] == sign and board[row_index][2] == sign):
            return True
    for col_index in range(len(board[0])):
        if(board[0][col_index] == sign and board[1][col_index] == sign and board[2][col_index] == sign):
            return True
    if(board[0][0] == sign and board[1][1] == sign and board[2][2] == sign):
        return True
    if(board[0][2] == sign and board[1][1] == sign and board[2][0] == sign):
        return True
    return False

def is_game_tie(board):
    if(len(free_board_indices(board))==0):
        print("DRAW..")
        return True
    return False
    
    
def free_board_indices(board):
    free_fields=make_list_of_free_fields(board)
    free_fields_index=list()
    for field in free_fields:
        free_fields_index.append(field[0]*3 + field[1] + 1)
    return free_fields_index
    
def draw_move(board):
    # The function draws the computer's move and updates the board.
    free_indices = free_board_indices(board)
    random_index=-1
    while random_index not in free_indices:
        random_index = randrange(8) + 1
    board[(random_index-1)//3][(random_index-1)%3]=COMPUTER
    print(COMPUTER + " plays: ")
    display_board(board)

board = [[3*i+j+1 for j in range(3)]for i in range(3)]
board[1][1]=COMPUTER
display_board(board)

#print(make_list_of_free_fields(board))
while not is_game_tie(board):
    enter_move(board)
    if(victory_for(board, USER)):
        print(USER + " wins!")
        exit()
    draw_move(board)
    if(victory_for(board, COMPUTER)):
        print(COMPUTER + " wins!")
        exit()