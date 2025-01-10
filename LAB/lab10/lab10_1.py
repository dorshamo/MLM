#use these strings:

#Enter a string, please:
#The most frequent letter is
#Thank you for exploring strings and complexity
def most_frequent(string):
    '''
    Checks what letter appears the most times and returns it

    Parameters
    ----------
    string : str
        the string we enter to the function.

    Returns
    -------
    str
        the letter who appears most time or -1 if there is no letters in the string.

    '''
    lst = [0]*26
    max_appears = 0
    max_letter = ''
    letter_num = 0
    for letter in string:
        if letter >= 'A' and letter <= 'Z':
            letter = chr(ord(letter)-ord('A')+ord('a'))
        if letter >= 'a' and letter <= 'z':
            letter_num = ord(letter) - ord('a')
            lst[letter_num]+= 1
        if lst[letter_num] > max_appears and (letter >= 'a' and letter <= 'z'):
            max_appears = lst[letter_num]
            max_letter = letter
        elif lst[letter_num] == max_appears and (letter >= 'a' and letter <= 'z'):
            if max_letter > letter:
               max_appears = lst[letter_num]
               max_letter = letter
    if max_appears == 0:
        return '-1'
    return max_letter
            
def main():
    """ main function for the input of the string and loop antil the input is quit """
    string = input("Enter a string, please: ")
    while string != "quit" and string != "Quit":
#calling for the function to find the letter that appears most times in the string
        most_frequent_letter = most_frequent(string)
        if most_frequent_letter == '-1':
            print(most_frequent_letter)
        else:
            print("The most frequent letter is",most_frequent_letter)
        string = input("Enter a string, please: ")
    print("Thank you for exploring strings and complexity")
        
main()
    
    