def main():
#creating input for a natural number and put it in Variable.
    print("Enter a natural number: ", end='')
    num = int(input())
#creating a Variable to store the numbers that we want to sum.
    sum_num = 0
#creating a while loop to collect all the numbers until we get to the number of the input.
    for i in range(0,num+1):
        if i < num+1:
            sum_num = sum_num + i
#printing the triangke number that we found after we adds up all the numbers.
    print("The triangle number in location",num,"is:",sum_num)
      
main()
    
    
    
    
    