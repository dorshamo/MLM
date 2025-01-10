# Enter elements:
# The List:
# Enter new number:
# The New List:
def new_list_sorted(lst,n):
    """
    adding to the list the extra number.
    
    Parameters
    ----------
    lst : int
        the list we put in the function.
    n : int
        the number we put in side the list

    Returns
    -------
    lst : int
        the list with the extra number.

    """
    amount_lst = len(lst)
    lst.append(lst[amount_lst-1]+1)
    i = len(lst)-2
    while i > 0 and lst[i] > n:
        lst[i+1] = lst[i]
        i-=1
        lst[i+1] = n
    return lst


def main():
# creating input for numbers and puts them inside a list
    print("Enter elements:")
    lst = []
    while len(lst)<5:
        elem = int(input())
        lst.append(elem)
    print("The List :",lst)
#input for new number.
    n = int(input("Enter new number: "))
# calling the function and printing the list with the new number.
    new_lst = new_list_sorted(lst,n)
    print("The new List:",new_lst)
    
main()   
    