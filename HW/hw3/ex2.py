"""
     Use the following printing strings:
                "Enter the size of the board (N >= 3): "
                "Enter the initial position (x, y): "
                "Invalid input !"                            - in case any invalide input
                "Start game board (step 0):"
                "Player X (step Y): from ( xx, xx) to (xx,xx)"
                Player B (step 4): from (xx, xx) no valid move
                "Player X lost the game "
                "End game board:"
               

"""

def matrix_0(board,N):
    '''
    create a matrix full of zeros.

    Parameters
    ----------
    board : list
        a list we enter the function.
    N : int
        the size we want the matrix to be.

    Returns
    -------
    board : list
        the matrix we return with the zeros.

    '''
    for i in range(N):
        row_board = []
        for j in range(N):
           row_board.append(0)
        board.append(row_board)
    return board



def board_view(board):
    '''
    

    Parameters
    ----------
    board : list
        the matrix we want to print.

    Returns
    -------
    returns the print of the board.

    '''
    for row in board:
       for cell in row:
          print(cell, end=' ')
       print()
  


def is_valid_move(board,x,y):
    '''
    

    Parameters
    ----------
    board : list
        the matrix of the board.
    x : int
        the row location.
    y : int
        the column location.

    Returns
    -------
    bool
        if the move inside the board its a valid move.

    '''
    if x >= 0 and x < len(board) and y >= 0 and y < len(board) and board[x][y] == 0:
        return True
    return False




def get_possible_move(board, x, y):
    '''
    

    Parameters
    ----------
    board : list
        the board with the zeros.
    x : int
        the row loction.
    y : int
        the column location.

    Returns
    -------
    possible_move : list
        returns a list of all the possible moves.

    '''
    possible_move = []
    moves = [[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2],[-2,-1]]
    for move in moves:
        new_x, new_y = x + move[0], y + move[1]
        if is_valid_move(board, new_x, new_y):
            possible_move.append((new_x, new_y))
    return possible_move

"""main function for the structure of the game"""
def main():
#if the inputs are invalid, prints a massage
    N = int(input("Enter the size of the board (N >= 3): "))
    x, y = eval(input("Enter the initial position (x, y): "))
    if N < 3 or  x<= 0 or y <= 0:
        print("Invalid input !!")
#if the input valid, start the game with a view of the board.
    else:
        board = []
        board = matrix_0(board, N)
        step_count = 1
        board[x-1][y-1] = step_count
        print("Start game board (step 0): ")
        board_view(board)
        player_a = "Player A"
        player_b = "Player B"
        current_player = player_a

#flag to know when the game needs to end
        end_game = False
        while not end_game:
            possible_moves = get_possible_move(board, x-1, y-1)  

#if the game ends, print this massages
            if not possible_moves:
                print(current_player, " (step ", step_count, "): from (",x, ",",y, ") no valid move",sep='')
                print(current_player,"lost the game")
                print()
                print("End game board")
                board_view(board)
                end_game = True
#until the game stops every turn print the move, and go with the steps.   
            else:
                new_x, new_y = possible_moves[0]
                step_count += 1
                board[new_x][new_y] = step_count
                print(current_player, " (step ", step_count-1, "): from (",x, ",",y, ") to (", new_x + 1, ",", new_y + 1, ")", sep='')
                x = new_x
                y = new_y
                if current_player == player_a:
                  current_player = player_b
                else:
                  current_player = player_a
                x, y = new_x + 1, new_y + 1  
        
main()     
