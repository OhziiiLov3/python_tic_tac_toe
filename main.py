# Tic Tac Toe Project 
# This Project helps build fundmental skills and concepts of Python 
""" 

Tic Tac Toe Board 3 x 3 box which consists of an array w/ 3 nested arrays containing 3 elements each 
[
    [-,-,-],
    [-,-,-],
    [-,-,-],

]

user_input -> something 1-9
if anything else: tell user to enter another value 
check if user_input is already taken 
add user_input to the board 
check if user won: checking rows, columns and diagionals 
toggle between users upon successful 

"""

# from sqlite3 import Row
# from threading import active_count


from bdb import Breakpoint


board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"],

]

user = True # when true it refers to x, otherwise 
turns = 0 

# How to print a tic-tac-toe board template 
def print_board(board):
    for row in board:
        for slot in row:
            print(f"{slot} ",  end="")
        print()

print_board(board)
# Function to improve control flow, if user inputs == q we exit the loop 
def quit(user_input):
    if user_input.lower() == "q": 
        print("Thanks for Playing")
        return True
    else: 
        return False

def check_input(user_input):
# Check if input is a number 
    if not isnum(user_input): 
        return False
    user_input = int(user_input)
# Check if number is 1-9 
    if not bounds(user_input): 
        return False 

    return True 

def isnum(user_input):
    if not user_input.isnumeric():
        print("This is not a valid number")
        return False
    else:
        return True 

def bounds(user_input):
    if user_input > 9 or user_input < 1:
        print("This number is out of bounds")
        return False
    else:
        return True 

def istaken(coords,board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "_":
        print("This positon is Taken")
        return False
    else: 
        return True

def corrdinates(user_input):
    row = int(user_input / 3)
    col = user_input
    if col > 2:
        col = int(col % 3)
    return (row,col)

def add_to_board(coords, board, active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

# toggle between users upon successful
def current_user(user):
    if user: 
        return "x"
    else:
        return "o"
# check if user won: checking rows, columns and diagionals
def iswin(user,board):
    if checkrow(user, board): 
        return True 
    if check_col(user, board):
        return True  
    if check_diag(user,board):
        return True
    return False

def checkrow(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False 
                break
        if complete_row:
            return True
    return False 

def check_col(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False 
                break 
        if complete_col: 
            return True
    return False 

def check_diag(user, board):
    # top left to bottom right 
    if board[0][0] == user and board[1][1] == user and board[2][2]:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] ==user:
        return True
    else: 
        return False  

# We start are program with an infinte loop(True), the loop breaks if the user inputs q
while turns < 9:
    active_user = current_user(user)
    print_board(board)
    user_input = input("Enter a Position 1-9 or Enter \"q\" to quit: ")
    if quit(user_input): 
        break
    if not check_input(user_input):
        print("Please try Again")
        continue
    user_input = int(user_input) - 1
    coords = corrdinates(user_input)
    if istaken(coords, board):
        print("Please try Again")
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user, board):
        print(f"{active_user.upper()} won!")
        break
    turns += 1
    if turns == 9: 
        print("Tie!")
    user = not user 







