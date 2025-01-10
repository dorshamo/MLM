def main():
#creating input for a natural number.
    print("Enter a natural number: ", end='')
    num = int(input())
#creating variables for the amount of divisors and the divisors.
    amount_divisors = 0
#divisors equal to one because we need can't divide with zero.
    divisors = 1
#if statement do sort the natural numbers
    if num < 0:
        print("Input is not a natural number")
    else:
#while statement to find all the divisors.
        print("The list of natural divisors of",num,"is: ",end=' ')
        while divisors < num+1:
#if statment to find the numbers that num modulo give us zero.
            if num % divisors == 0:
                print(divisors,end=' ')
#store the the amount in his varieble.
                amount_divisors += 1
            divisors += 1
#printing the amount of divisors and all the divisors.
        print("\nThe amount of divisors is:",amount_divisors)
    
main()