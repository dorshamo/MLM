def smallest_letter(string):
    '''
    checks whats the smallest letter in the string.

    Parameters
    ----------
    string : str
        the string we checking.

    Returns
    -------
    smallest : str
        the smallest letter we found or space if we didnt find.

    '''
    smallest = 'z'  
    for letter in string:
        if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            if letter.lower() < smallest:
                smallest = letter.lower()
    if smallest == 'z':  
        smallest = ''
    return smallest

def largest_letter(string):
    '''
    checks whats the largest letter in the string.

    Parameters
    ----------
    string : str
        the string we checking.

    Returns
    -------
    largest : str
        the smallest letter we found or space if we didnt find.

    '''
    largest = 'a'  
    for letter in string:
        if 'a' <= letter <= 'z' or 'A' <= letter <= 'Z':
            if letter.lower() > largest:
                largest = letter.lower()
    if largest == 'a':  
        largest = ''
    return largest


"""main function to ask for string and calling for the function to find the biggest and smallest letters in the string."""
def main():
    string = input("Enter your sentence: ")
    largest = largest_letter(string)
    smallest = smallest_letter(string)
    if largest == '' and smallest == '':
        print("There were no letters")
    else:
        print("Largest and smallest letters are:", largest, smallest)

main()