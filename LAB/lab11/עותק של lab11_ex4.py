# Please enter a string:
# The string "123" corresponds to the number 123.
# The string is illegal!
def check_num(string):
    '''
    

    Parameters
    ----------
    string : TYPE
        DESCRIPTION.

    Returns
    -------
    TYPE
        DESCRIPTION.

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
    string = input("Please enter a string: ")
    temp = ''
    for char in string:
        if char < '0' or char > '9':
            temp = char
    if temp != '':
      print("The string is illegal!")
    else:
        num = check_num(string)
        print('The sting "',string,'" corresponds to the number ',num, sep='')
        
main()