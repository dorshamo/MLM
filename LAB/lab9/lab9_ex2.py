def string_fix(string):
    '''
    function that fix the old string by "removing" 
    the a letter that repeats itself one after the other.

    Parameters
    ----------
    string : str
        the old string we put in the function

    Returns
    -------
    new_string :str
        the new string without the repeating letters the we return.

    '''
    new_string = ''
    for num in range(len(string)):
        if num == (len(string)-1) or string[num] != string[num+1]:
            new_string += string[num]
    return new_string
            


"""main function to ask for string and calling for the fix function"""
def main():
    string = input("Enter a string, please: ")
    new_string = string_fix(string)
    print("After removing all duplicates:",new_string)
    
main()

