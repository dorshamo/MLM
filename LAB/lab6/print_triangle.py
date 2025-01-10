# use the following strings:

# "*** Triangle  ***"
# "Enter a letter:"
# "Enter an integer:"

"""
        This function uses a given character to print triangle which:
                - is right-angled 
                - has 2 equal sides
        
        Input:
                 - letter - the character for the printing
                 - num    - the size of the right angle triangle sides 
                 
""" 
#function with two loops to create the triangle
def print_triangle(num,letter):
    for i in range(num,0,-1):
        for j in range(i):
            print(letter,end='')
        print()

#main function to take an input for the letter and the number and to call the triangke function.  
def main():
   letter = input("Enter a letter: ")
   num = int(input("Enter an integer: "))
   print("*** Triangle  ***")
   print_triangle(num,letter)

main()

   