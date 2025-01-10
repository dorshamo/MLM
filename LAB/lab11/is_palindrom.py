# Enter a sequence of natural numbers,end with 0:
# The list of digits is a Palindrom
# The list of digits is not a Palindrom

def is_palindrom(lst):
    '''
    function that returns true if any two members of it that are at equal 
    distances from its beginning and end, are equal to each other (palindrome).

    Parameters
    ----------
    lst : list
        the list that we want to check.

    Returns
    -------
    bool
        return true if the function is palindrome and false if he isnt.

    '''
    n = len(lst)
    if lst == []:
        return True
    if lst[0] == lst[n-1]:
        return is_palindrom(lst[1:-1])
    else:
        return False
    
def num_lst(num):
    '''
    function that takes a number and turn it in to a list.
    (because we looking for palindrome it doesn't matter if the list is in the opposite direction)

    Parameters
    ----------
    num : int
        the number we want to turn in to a list.

    Returns
    -------
    lst : list
        a list of all the digits in side the number.

    '''
    lst = []
    while num != 0:
        lst.append(num%10)
        num//=10
    return lst
        

def main():
    ''' main function to ask for the numbers from the user and print th right messeges with the functions '''
    print("Enter a sequence of natural numbers,end with 0: ")
    num = int(input())
    while num != 0:
        lst = num_lst(num)
        if is_palindrom(lst):
          print("The list of digits is a palindrom")
        else:
          print("The list of digits is not a palindrom")
        num = int(input())
    print("FINISH")
main()
        
        
        
        
        