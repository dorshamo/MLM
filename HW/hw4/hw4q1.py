


def check_parentheses(user_input,num):
    """
    take the string we entered and check if the emount of parentheses 

    Parameters
    ----------
    user_input : str
        Dthe string we want to check
    num : int
        a variable to know If every opening bracket has a corresponding bracket

    Returns
    -------
    bool
        return true If every opening bracket has a corresponding bracket and false if not

    """
    b = False
    if num<0:
        return b
    else:
        if user_input == '': 
          if num == 0:
            b = True
            return b
          else:
              return b
        elif user_input[:1] == '(':
            num+=1
            return check_parentheses(user_input[1:], num)
        else:
            num-=1
            return check_parentheses(user_input[1:], num)
    
    
        
        

#do not change main!
def main():
    user_input = input("Enter a parentheses string: ")
    print(check_parentheses(user_input,0))
    
main()
