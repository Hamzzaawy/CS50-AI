"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

row = 3
column = 3


def initial_state():
    """
    Returns starting state of the board.
    """
    
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    # loop on the two dimentional array counting the X's and O's then compare them and returns the higher count
    for i in range(row):
        for j in range(column):
            if board[i][j] == "X":
                countX += 1
            elif board[i][j] == "O":
                countO += 1
    if countX > countO: 
        return "O"
    elif countO >= countX:
        return "X"



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # create a set and loop on the two dimentional array then check if there is a none spot in the array then add it to the set else skip this 
    # itteration then return the calculated set
    output = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] != None:
                continue
            else:
                output.update([(i,j)])
    # print(output)
    return output



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # makes a deep copy of the board and check the next player to play and add his simpole in the postion marked by the action tuple
    cpyBoard =copy.deepcopy(board)
    nextPlayer = player(board)
    i = action[0]
    j = action[1]
    if nextPlayer == "X":
       cpyBoard[i][j] = "X"
    else:
        cpyBoard[i][j] = "O"
     
    # print(cpyBoard)
    return cpyBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # checks if the game conditions of finishing is met by calling the terminal function if not it will break and return 
    # if not check who has won usning the utility function that determine who has won subscribing the winner with a number 1 for X and -1 for O
    if terminal(board) == False:
        return None
    else:
        if utility(board) == 1:
            # print("the winner is X")
            return "X"
        elif utility(board) == -1:
            # print("the winner is O")
            return "O"
        else:
            return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # checks if there is a winner by calling the utility if so it return else checks for emty slots if so it retuens false if there is no 
    # empty slots it will return true
    if utility(board) != 0:
        return True
    else:
        for i in range(row):
            for j in range(column):
                if board[i][j] == None:
                    return False
    return True

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # calculates the state of the board if 1 means X has won and if -1 then O has won else there is no one won and it returns the calculated
    # value
    # it does so by checking the 8 possible combination to have a winner first by having a three consictive simpole in a row (3)or in a column(3)
    #  or in diagonal (2) 
    
    check = -1                  # healping variable

    for k in range(4):
        
        #checking the \ diagonal by saving the first element of it to a variable and checking the equality in the rest of the diagonal
        #and returning a number represents that conclusion if correct
        if k == 0:
            if board[0][0] != None:
                temp = board[0][0]
                if temp == board[1][1]:
                    if temp == board [2][2]:
                        check = k

        #checking the / diagonal the same way as the \ diagonal
        elif k == 1:
            if board[0][2] != None:
                temp = board[0][2]
                if temp == board[1][1]:
                    if temp == board [2][0]:
                        check = k

        # checking the columns by looping on the three column anc check if there is equality in one of them and return the number represents
        # column check and also returns a number represents which cloumn of the three in order to check the equality was X or O
        elif k == 2:
            for i in range(3):
                if board[i][0] != None:
                    temp = board[i][0]
                    for j in range(3):
                        # print(f"i = {i}, j ={j}")
                        if temp == board[i][j]:
                        
                            if j == 2:
                                check = k
                                index = i
                            continue
                        else:
                            break
        # checking the rows the same way as the column
        elif k == 3:
            for i in range(3):
                if board[0][i] != None:
                    temp = board[0][i]
                    for j in range(3):
                        # print(f"i = {i}, j ={j}")
                        if temp == board[j][i]:
                        
                            if j == 2:
                                check = k
                                index = i
                            continue
                        else:
                            break

    # print(check)

    if check == 0:
        if board [0][0] == "X":
            return 1
        else:
            return -1

    elif check == 1:
        if board [0][2] == "X":
            return 1
        else:
            return -1

    elif check == 2:
        if board [index][0] == "X":
            return 1
        else:
            return -1

    elif check == 3:
        if board [0][index] == "X":
            return 1
        else:
            return -1

    else:
        return 0

    

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # check which player's turns to play it it is X then assume that the outcome is -1 that O is the winner and try to reverse the outcome 
    # by assuming that O is the next turn and will try to minimize the score and then direct the game towards a higer outcome close to 1 or 
    # at least 0 and if it is O we do the reverse as O's aim to mimize the score
    # as the calculating takes a very large time we use alpha beta pruning to optimize the calculating by bassing to the function that calculate
    # the max the minimum value we reached up until the point of calculation in order to break the loop of calculating unessesary numbers as the
    # opponent aim is to take that minimum (check the slides for a graphical explaining )
    nextPlayer = player(board)
    output = []
    temp = []
    if nextPlayer == "X":
        v = -1
        last_H = v
        for action in actions(board):
            # print(action)
            var_x = MinValue(result(board, action),last_H)
            if  var_x > v:
                v = var_x
                temp = action
                last_H = v
        output = temp

    elif nextPlayer == "O":
        v = 1
        last_L = v
        for action in actions(board):
            # print(action)
            var_o = MaxValue(result(board, action),last_L)
            if  var_o < v:
                v = var_o
                temp = action
                last_L = v
        output = temp
        

    return output




def MaxValue(board,test):
    if terminal(board):
        return utility(board)
    v = -1
    for action in actions(board):
        temp_x = MinValue(result(board, action),v)
        # appling the alpha-beta purning as we check the low value passed by last calculation and if we find a value lower that this value 
        # we break the looping and retuen the passed value (test)
        if test <= temp_x :
            v = test
            break
        v = max (v, temp_x)
        # print(action)
    return v

def MinValue(board,test):
    if terminal(board):
        return utility(board)
    v = 1
    for action in actions(board):
        temp_o = MaxValue(result(board, action),v)
        # same as maxValue but in a revers manner
        if test >= temp_o:
            v = test
            break
        v = min (v, temp_o)
        # print(action)
    return v
