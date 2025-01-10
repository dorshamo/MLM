def check_matrix(matrix):
    '''
    checks if the matrix is square with o(1).

    Parameters
    ----------
    matrix : list
        the matrix we want to check.

    Returns
    -------
    square_matrix : bool
        return true if the matrix is square and false if not.

    '''
    square_matrix = False
    if len(matrix) == len(matrix[0]):
        square_matrix = True
    return square_matrix
        
            
    
def matrix_view(matrix):
    '''
    create the print of the matrix.

    Parameters
    ----------
    matrix : list
        the matrix we want to print

    Returns
    -------
    None.

    '''
    for row in matrix:
       for cell in row:
          print(cell, end='    ')
       print()
       

def is_extreme(matrix):
    '''
    checks if all the main diagnal bigger then the secondairy diagnal.

    Parameters
    ----------
    matrix : str
        the matrix we want to check.

    Returns
    -------
    bool
        if the matrix is extreme we return true.

    '''
    if check_matrix(matrix):
        n = len(matrix)
        for i in range(n):
            if matrix[i][i] < matrix[i][n-i-1]:
                return False
        return True
    return False
        


def main():
    ''' main function to call the functions and create all the prints for the matrix'''
    print('first matrix:')
    m_1=[[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5],[6,7,8,9,0],[1,2,3,4,5]]
    matrix_view(m_1)   
    answer = is_extreme(m_1)
    print('is extreme matrix:',answer) 
    
    
    print('second matrix:')
    m_2=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[1,2,3,4,5]]
    matrix_view(m_2)   
    answer = is_extreme(m_2)
    print('is extreme matrix:',answer)
    
    
    
    print('third matrix:')
    m_3=[[5,2,3,4,2],[6,7,8,3,0],[1,2,4,4,5],[6,0,8,9,0],[1,2,3,4,5]]
    matrix_view(m_3)
    answer = is_extreme(m_3)
    print('is extreme matrix:',answer)
    
    
    
    print('fourth matrix:')
    m_4=[[1]]
    matrix_view(m_4)
    answer = is_extreme(m_4)
    print('is extreme matrix:',answer)
    
      
main()

