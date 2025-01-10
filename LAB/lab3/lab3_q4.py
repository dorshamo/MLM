
def main():
    #create an imput to enter 4-digits integer
    num=int(input("Please enter 4-digits integer: "))
    #separates beteen the first two numbers and the last two
    num_1 = num//100
    num_2 = num%100
    #print the number with the new order
    print("New number : ",num_2*100+num_1, sep='')
    #checks which number has an odd digit
    units = num%2
    tens = num//10%2
    hundreds = num//100%2
    thousands = num//1000%2
    #sybtracts the amount of odd numbers by 4 to find all the evens number
    even_numbers = 4-units-tens-hundreds-thousands
    print("The amount of even digits in the number",num,"is",even_numbers)
main()