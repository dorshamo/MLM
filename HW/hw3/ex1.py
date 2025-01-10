
def title(STR):
    """
    take a string and writt it so that it is in lowercase letters and capital letters with uppercase.

    Parameters
    ----------
    STR : str
        the sentence we entered to the function.

    Returns
    -------
    new_str : str
        return the sentecnce after the fixeses.

    """
    new_str = ""
    capital_next = True

    for letter in STR:
        if letter >= 'a' and letter <= 'z':  
            if capital_next:
                new_str += chr(ord(letter) - (ord('a') - ord('A')))
                capital_next = False
            else:
                new_str += letter
        elif letter >= 'A' and letter <= 'Z':
            if capital_next:
               new_str += letter
               capital_next = False
            else:
                new_str += chr(ord(letter) + (ord('a') - ord('A')))
        else:
           new_str += letter
           capital_next = True
            

    return new_str
""" main function with the list of strings and calling the function with a loop to check and fix all of them."""
def main():
    lst_str = ['Have a  wonderful \t\t day!!', '1 and 2 are 3three!', 'WHAT ARE \nYOU \tdOING??', 'ONEWORD','tricky ONE','^awsome^']
    for STR in lst_str:
        print("Original string:     ", STR)
        new_str = title(STR)
        print("Title string:     ", new_str)
    print("FINISH")

main()
