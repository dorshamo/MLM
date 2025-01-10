def all_letters(string):
    '''
    checks if there is a character thats not in the "abc" and returns false in that case.

    Parameters
    ----------
    string : str
        the string we want to check 

    Returns
    -------
    bool
        return false if there is a character thats not in the "abc" and true there in no such character.

    '''
    if string == '':
        return True
    else:
        if (string[0] >= 'a' and string[0] <= 'z') or (string[0] >= 'A' and string[0] <= 'Z'):
          return all_letters(string[1:])
        else:
          return False
    
def main():
    """ main function to ask the user for input and print the right messege after calling the all_letters function. """
    
    string = input("Please enter a string: ")
    if all_letters(string):
        print("The string is legal")
    else:
        print("The string is illegal")
    
main()