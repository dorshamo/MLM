def gcd(a,b):
    """
    compute the greatest common divisor (GCD) of two integers.


    Parameters
    ----------
    a : int
        the first integer.
    b : int
        The second integer.

    Returns
    -------
    int
        the greatest common divisor of 'a' and 'b'.

    """
    if not b:
        return a
    else:
        return gcd(b, a % b)
                
def sym_not_coprime(lst):
    """
    determine if the elements of a list are symmetrically not coprime.

    Parameters
    ----------
    lst :list
        The list of integers to check.

    Returns
    -------
   bool
        True if the elements are symmetrically not coprime, False otherwise.

    """
    if len(lst) == 1: 
        return True
    if lst[0] == lst[-1] and gcd(lst[0] , lst[-1]) != 1 :
        return sym_not_coprime(lst[1:-1]) 
    else:
        return False
    
def sym_not_coprime_lists(lst):
    """
    determine if a list of lists has symmetrically not coprime elements.

    Parameters
    ----------
    lst : list
        the list of lists to check.

    Returns
    -------
    bool
        True if the elements are symmetrically not coprime, False otherwise.

    """
    if len(lst) == 0:
        return True
    elif sym_not_coprime(lst[0]):
        return sym_not_coprime_lists(lst[1:])
    else:
        return False 

def print_nested_list(lst):
    """
    Print a nested list.


    Parameters
    ----------
    lst : list
        The nested list to print.

    Returns
    -------
    int
        The length of the nested list.

    """
    if len(lst) == 0:
        return 0
    for num in lst[0]:
        print(' ',num, end=' ')
    print()
    print()
    return print_nested_list(lst[1:])
    
def main():
    lst_of_lsts=[]
    num_of_lst = int(input("Enter number of lists, please: "))
    print()
    for lst in range(num_of_lst):
        print()
        print("Enter length of list no.",lst,", please: ",end='')
        length_of_lst =  int(input())
        print()
        if length_of_lst == 1:
            print("Enter",length_of_lst,"integer, please: ")
        else:
            print("Enter",length_of_lst,"integers, please: ")
        lst_1 = []
        for length in range(length_of_lst):
            print()
            num = int(input())
            lst_1.append(num)
        lst_of_lsts.append(lst_1)
    print()
    print("List of lists: ")
    print()
    print_nested_list(lst_of_lsts)
    print()
    if sym_not_coprime_lists(lst_of_lsts):
        print("Has no pair of coprime numbers in symmetric locations.")
    else:
        print("Has at least one pair of coprime numbers in symmetric locations.")
    print()
    print("Thank you for exploring GCD and list of lists using recursion.")
main()
