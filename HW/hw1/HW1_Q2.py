#function definition for finding the perfect number.
def perfect_num(num):
    perfect_num = 0
#for loop to check all the numbers from 1 to the number which one divisible without a remainder and sum it.
    for i in range(1,num):
        if num % i == 0:
            perfect_num += i
#if the sum is equal to the original number its a perfect number.
    return perfect_num == num


#function definition for finding if there is double of digits in the number and return the biggest.
def double_dig_num(num):
    temp_double = 0
    double = 0
#while loop that take the two first number to check if thay are the same and every time move one digit left.
    while num > 9:
          two_digits = num%100
#if statement to check if the two numbers equal and save the digit.
          if two_digits%11 == 0:
             temp_double = two_digits%10
#if statement to take the bigest number that as double.
             if temp_double > double:
                 double = temp_double 
#divides the number by 10 to seperate it from the unit digit.
          num//=10
#return the bigest double.
    return double
            
  
#function definition to find a simetric number.         
def simetric_num(num):
    rev_num = 0
    copy_num = num
    count = 0
#while loop to reverse the input number and to find the amount of digits.
    while  copy_num > 0:
         unit = copy_num % 10
         rev_num = rev_num*10 + unit
         copy_num//=10
         count = count + 1
#devide the count by two to now how mant time we need to check the unit digits.
    new_count = count//2
#while loop to check the units digits of the number and the revers number if they are divisible by each other.
#we use the new count to now when the loop can be stopped/
    while new_count > 0.5:
        if (num%10)%(rev_num%10)!=0 and (rev_num%10)%(num%10)!=0:
            return False
        else:
             num//=10
             rev_num//=10
        new_count-=1
#if the number simetric we return True and of not we return False.         
    return True
 
            
def main():
#creating input for a number.
    print("Please enter a number: ", end='')
    num = int(input())
#if statement to ensure that the input is natural number.
    if num <0:
        print("Illegal input")
    else:
#creating input for the letters we want for the menu.
        print("Select operation: ")
        print("p   -   checks if the number is perfect")
        print("D   -   checks if the number has a double digit")
        print("S   -   checks if the number is simetric")
        operation = input()
#if statement for every letter and to insure that only the three letter can be chosen.
#the second if statement is to call the function and print the right message.
        if operation == 'P':
            if perfect_num(num):
                print(num,"is a perfect number")
            else:
                print(num,"is not a perfect number")
        elif operation == 'D':
            result = double_dig_num(num)
            if result:
                print("The max double digit is:",result)
            else:
                print("No double digit in number",num)
        elif operation == 'S':
            if simetric_num(num):
                print(num,"is a simetric number")
            else:
                print(num,"is not a simetric number")
        else:
            print("Illegal input")
main()
