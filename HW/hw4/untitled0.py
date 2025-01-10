def gcd(x,y):
    if y == 0:
        return x
    return gcd(y,x % y)


def sym_not_coprime(lst):
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

    b = True
    n = len(lst)
    if lst == []:
        return b
    elif gcd(lst[0], lst[n-1]) != 1:
        lst = lst[1:-1]
        b = sym_not_coprime(lst)  
        return b
    else:
        if lst[0] != 1 and lst[n-1] != 1:
            b = False
        return b
        
          
def sym_not_coprime_lists(lst_of_lsts):
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
    if len(lst_of_lsts) == 0:
        return 
    for num in lst_of_lsts[0]:
        print(' ',num, end=' ')
    print()
    print()
    return print_nested_list(lst_of_lsts[1:])
   

def main():
    lst_of_lsts = [[10,9,9,3,5],[256,11,15,121,2],[7,21],[2,100,64,9,45,16,500,32]]
    lst_of_lsts =[[1,2,3,4,5,8,9,16,1],[2,9,16,25,36,30,10,44,54,32],[11,12,36,33],[15,16,4,40,18],[6]]
    # lst_of_lsts =[[10,9,9,3,5],[256,11,15,121,2],[7,21],[2,100,64,9,45,16,500,32]]
    # lst_of_lsts = [[1]]
    # lst_of_lsts = [[15],[14,126],[14,1,126]]
    # lst_of_lsts = [[45,2,3,4,5,8,9,26,54],[2,9,16,25,36,60,10,44,54,32],[11,12,36,33],[15,16,4,40,18],[7]]
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