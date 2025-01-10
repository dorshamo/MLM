"""
Multi Line comments...

File name: lab4_q1.py
Description: ...
"""

#single line comment
def main():
#creating a input for 4-digits number.
    num = int(input("Please enter a 4-digits natural number: "))
# seperate each cheracter.
    units = num%10
    tens = num%100//10
    hundreds = num//100%10
    thousands = num//1000
#creating a if statemant to sort the numbers that we are looking for.
    if num>0 and (num<1000 or num>=10000):
        print(num,"isn't a 4-digits number.")
    elif num<0:
        print(num,"isn't a natural number.")
#sort with if statemant all the kinds of sequences that we are looking for.
    else:
        if thousands == hundreds and hundreds == tens and tens == units:
            print("All digits are the same.")
        elif (units - tens)==(hundreds - thousands)==(tens - hundreds) and (thousands >= hundreds >= tens >= units):
            print("Decreasing arithmetic sequence.")
        elif thousands >= hundreds and hundreds >= tens and tens >= units:
            print("Decreasing sequence.")
        elif(thousands - hundreds)==(tens - units)==(hundreds - tens) and thousands <= hundreds <= tens <= units: 
            print("Increasing arithmetic sequence.")
        elif thousands <= hundreds and hundreds <= tens and tens <= units:
            print("Increasing sequence.")
        else:
            print("Not increasing and not decreasing.")

main()