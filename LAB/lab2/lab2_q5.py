def main():
    letter = input("please enter a char: ")
    letter = ord(letter)
    Next_letter = (letter - ord('a') + 1) % 26 + ord('a')
    print("Next letter is:",chr(Next_letter))
main()
