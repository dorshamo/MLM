#Enter integer:
#The digit 2 appears 2 times
#The most frequent digit/s is/are:
#It occurs times 
def main():
# input for a number and creating a loop for the option of number equal to zero or not
    print("Enter integer : ",end='')
    num = int(input())
    while num !=0:
        cnt_lst = [0]*10
        a_num = num
# if statement to take the absolute value of the number
        if num < 0:
            a_num*=-1
# crating the list of the amount of time every digit is in the number.
        while a_num>0:
            dig = a_num%10
            cnt_lst[dig]+=1
            a_num//=10
            max_freq = 0
            max_digits = 0
#printing the times every digit is in the number and chaking for the digit with the most repetitions
        for i in range(10):
            if cnt_lst[i] > 0:
               print("The digit",i,"appears",cnt_lst[i],"times")
               if cnt_lst[i] > max_freq:
                  max_freq = cnt_lst[i]
                  max_digits = [i]
               elif cnt_lst[i] == max_freq:
                   max_digits.append(i)
#printing the most frequent number athe he's occurs times
        print("The most frequent digit/s is/are :",max_digits)
        print("It occurs times ",max_freq)
#asking for new number in the loop until we get zero.
        num = int(input("Enter integer : "))
#the prints for the option zero after we ends the loop.
    if a_num == 0:
       cnt_lst[0] = 1
       print("The digit",a_num,"appears",cnt_lst[0],"times")
       print("The most frequent digit/s is/are : ",a_num)
       print("It occurs times",cnt_lst[0])
main()



                    
                    
        
               

    

