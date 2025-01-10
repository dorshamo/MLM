"""
Dear students, for your convenience, attached strings to be used.
Notice that there is a difference in the strings if there is only one element in a list or more than one element.
Having '_' in a string meaning that a relevant integer number has to be determined in a run time.
"""
#Enter number of lists, please:
#Enter length of list no. _, please: 
#Enter 1 integer, please: 
#Enter _ integers, please: 
#List of lists:
#Has at least one pair of coprime numbers in symmetric locations.
#Has no pair of coprime numbers in symmetric locations.
#Thank you for exploring GCD and list of lists using recursion.
"""
Add doccumentation in the code and near every function explain in details (including meaning) what are the paramerers it gets ,
what it does, and what does it return.
"""




def gcd(x,y):
    '''
    

    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
    
    Parameters
    ----------
    x : int
        The first integer.
    y : int
        The second integer.

    Returns 
    -------
    int
    The greatest common divisor of x and y.

    '''
    if y == 0:
        return x
    return gcd(y,x % y)




def sym_not_coprime(lst):
    '''
    Checks if the list Has no pair of coprime numbers in symmetric locations.

    Parameters
    ----------
    lst : list
        the list of integers we want to check.

    Returns
    -------
    bool
        return false if there is one or more pairs of coprime numbers and true if not.

    '''
    n = len(lst)
    if lst ==[]:
        return True
    
    elif gcd(lst[0], lst[n-1]) !=1:
        return sym_not_coprime(lst[1:-1])
    else:
        if n == 1:
            return True
        else:
            False
        
          
        
        
def sym_not_coprime_lists(lst_of_lsts):
    '''
    

    Checks if there is at least one pair of coprime numbers in symmetric locations in each list within lst_of_lsts.
    
    Parameters
    ----------
    lst_of_lsts : list
        the list of all the lists that the user input.

    Returns
    -------
    bool
     return false if there is one or more lists with pairs of coprime numbers and true if not.
        

    '''
    if not lst_of_lsts:
        return True  
    else:
        lst = lst_of_lsts[0]
        lst_true_or_false = sym_not_coprime(lst)
        if not lst_true_or_false:  
            return False  
        else:
            return sym_not_coprime_lists(lst_of_lsts[1:]) 
   
    
   
        
def print_nested_list(lst_of_lsts):
    '''
    print all the lists in the list.

    Parameters
    ----------
    lst_of_lsts : list
        the list with all the list we want to print.

    Returns
    -------
    print
        the print of all the lists.

    '''
    if len(lst_of_lsts) == 0:
        return 
    for num in lst_of_lsts[0]:
        print(' ',num, end=' ')
    print()
    print()
    return print_nested_list(lst_of_lsts[1:])
           

        
def main():
    """
   Main function ask from the user for inputs to create list of lists, checks with the functions 
   for pair of coprime numbers and print the results

   """
    lst_of_lsts=[]
    num_of_lst = int(input("Enter number of lists, please: "))#the creation of the list
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
    print_nested_list(lst_of_lsts)#calling for the print function to print the lists
    print()
    if sym_not_coprime_lists(lst_of_lsts):# colling for the function to check for the pair of coprime numbers
        print("Has no pair of coprime numbers in symmetric locations.")
    else:
        print("Has at least one pair of coprime numbers in symmetric locations.")
    print()
    print("Thank you for exploring GCD and list of lists using recursion.")
main()

            
            
