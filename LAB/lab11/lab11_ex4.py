# Please enter a string:
# The string "123" corresponds to the number 123.
# The string is illegal!
def check_num(string):
    '''
    the function take a string with only numbers and returns the number as an integer.

    Parameters
    ----------
    string : str
        the snumber as string we want to change

    Returns
    -------
    int
        the number from the string as integer

    '''
    num = 0 
    if string == '':
        return num
    else:
        n = len(string)
        digit = ord(string[n-1]) - ord('0')
        remaining_num = check_num(string[:-1])
        if remaining_num == -1:
            return -1
        return digit + remaining_num * 10
    
def main():
    """main function to ask the user for a string of numbers and returns the number
      as a integer if the string with only numbers"""
    
    string = input("Please enter a string: ")
    temp = ''
    for char in string:
        if char < '0' or char > '9':
            temp = char
    if temp != '':
      print("The string is illegal!")
    else:
        num = check_num(string)
        print('The string "',string,'" corresponds to the number ',num, sep='')
        
main()