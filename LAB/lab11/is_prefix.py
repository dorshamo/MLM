# Enter a string:
# Enter another string:
# 123 is a prefix of 1234
# 1234 is not a prefix of 123
def is_prefix(pre_st, st):
    '''
    the funtion cheks if the first string is the prefix of the second string.

    Parameters
    ----------
    pre_st : str
        the string that we check if he's the prefix.
    st : str
        the string that we compere the first string to.

    Returns
    -------
    bool
        return true if pre_st is a prefix and false if not.

    '''
    if len(st) == len(st)-len(pre_st):
        return True
    if len(pre_st) == 0:
        return False
    else:
        if len(st)-1 > len(pre_st):
            if pre_st[0] == st[0]:
              return is_prefix(pre_st[1:], st[1:])
        else:
            return False
    
   
    
def main():
    ''' main function to ask for to strings and print the right messege by checking them with the is_prefix function.'''
    st = input("Enter a string: ")
    pre_st = input("Enter another string: ")
    if is_prefix(pre_st,st):
        print(pre_st,"is a prefix of",st)
    else:
        print(pre_st,"is not a prefix of",st)
main()