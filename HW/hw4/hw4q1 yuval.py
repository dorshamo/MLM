"""דור שמו - 207932740
                    יובל רוטנברג - 211877592
"""

def check_parentheses(str1,num):
    """
    check if the parentheses in the given string are balanced.

    Parameters
    ----------
    str1 : str
        the string containing parentheses to be checked.
    num : int
        counter for tracking the balance of parentheses.

    Returns
    -------
    bool
        True if the parentheses are balanced, False otherwise.

    """
    if str1 == "":
        return num == 0  
    if str1[0] == '(' :
        num += 1
    if str1[0] == ')':
        num -= 1
    
    
    if num < 0:
        return False
    else:
        return check_parentheses(str1[1:], num)
       

def main():
    user_input = input("Enter a parentheses string: ")
    print(check_parentheses(user_input,0))
    
main()


