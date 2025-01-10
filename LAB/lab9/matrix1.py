#use the following text:

#  Please enter the matrix elements:
#  The matrix is:
#  The matrix is legal!
#  The matrix is illegal!
def sumtrue(matrix, n):
    '''
    this function checks if the sum of the row equal to the number of row.

    Parameters
    ----------
    matrix : int
        the matrix we enter to the function.
    n : int
        the number of row we enter

    Returns
    -------
    bool
        if the sum equal to the number of row we return True.

    '''
    for row in matrix:
        Sum = 0
        for cell in row:
            Sum += cell
        if Sum == n:
            return True
    return False




def main_diagonal(matrix):
    '''
    checks if the main diagnol cells are all positive.

    Parameters
    ----------
    matrix : int
        the matrix we enter to the function.

    Returns
    -------
    bool
        if all the main diagnol cells are positive, we ruturn True.

    '''
    for i in range(len(matrix)):
        if matrix[i][i] <= 0:
            return False
    return True
   


"""main function to create the matrix from the elements we ask as input."""     
def main():
    matrix = []
    print("Please enter the matrix elements: ")
    for i in range(5):
        row_matrix = []
        for j in range(5):
            mt_el = int(input())
            row_matrix.append(mt_el)
        matrix.append(row_matrix)
    print("The matrix is:")
    print()
    for row in matrix:
        for cell in row:
            print("%5d"%cell, end='')
        print()
#we checks if the matrix is legal or not and return the right print.      
    legal = False
    for n in range(1, 6):
        if sumtrue(matrix, n) and main_diagonal(matrix):
            legal = True
    
    if legal:
        print("The matrix is legal!")
    else:
        print("The matrix is illegal!")

main()