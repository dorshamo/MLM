#Enter digits:
#The largest number is: 
#Input Error
def biggest_num(lst):
    """
    creaing the biggest number from all the integers inside the lst.

    Parameters
    ----------
    lst : int
        the list we entered to the function.
    Returns
    -------
    number : int
        the number we returend that we got from the list .

    """
    nt_lst = [0]*10
    for i in lst:
        nt_lst[i] += 1
    number = 0 
    for g in range(9,-1,-1):
        if nt_lst[g] > 0:
            num = nt_lst[g]
            while num > 0:
                number =  number * 10 + g
                num -=1
    return number


def main():
#creating iput for digits and checking that the number are between 0 to 9.
    print("Enter digists: ")
    num = int(input())
    lst = []
    if num <1 or num >9:
      print("Input Error")
    else:
#creating a list with the nubers and calling for the function to find the biggest number.
        while num != -1:
            lst.append(num)
            num = int(input())
        n = biggest_num(lst)
#printing the biggest number.
        print("The largest number is:",n)

main()       
        