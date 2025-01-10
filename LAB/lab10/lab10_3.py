#use the following strings:

#Please enter ordered and shifted sequence of numbers (end with -1): 
#The smallest number is:
def minShiftList(lst,lst_size):
    '''
    

    take a list and its sizev and find the smallest number with O(log n) – Logarithmic time complexity.
    ----------
    lst : list
        the ordered and shfted sequence of number.
    lst_size : int
        the size of the list.

    Returns
    -------
    int
        the smallest number.

    '''
    low = 0
    high = lst_size - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[high]:
            low = mid + 1
        elif lst[mid] < lst[high]:
            high = mid
        else:
            high -= 1
    return lst[low]
        
    
def main():
    """main function to create the list with inputs"""
    lst = []
    lst_size = 0
    print("Please enter ordered and shifted sequence of numbers (end with -1): ")
    num = int(input())
    while num != -1:
        lst.append(num)
        lst_size+=1
        num = int(input())
    smallest = minShiftList(lst,lst_size)
    print("The smallest number is:",smallest)
main()