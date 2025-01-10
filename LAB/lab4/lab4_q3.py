"""
Multi Line comments...

File name: lab4_q1.py
Description: ...
"""

#single line comment
def main():
#creating input for children,salary,sevice.
  children = int(input("Number of children: "))
  salary = int(input("Monthly salary: "))
  military_civil_service = input("Military, or civil service(enter character Y, or y for yes, otherwise any other character)? ")
#calculating mortgage 1 and mortgage 2.
  mortgage_1 = salary*0.25
  mortgage_2 = salary*0.35
#creating if statement to sort the approvel of mortgage.
  if salary >= 17500:
      print("The mortgage is approved with monthly payment of ","%.2f"%mortgage_2,".", sep='')
  elif ((military_civil_service =='y' or military_civil_service == 'Y') and salary >= 15000) or (children >= 5 and salary>=14000):
      print("The mortgage is approved with monthly payment of ","%.2f"%mortgage_1,".", sep='')
  else:
      print("Sorry, the mortgage is not approved.")

main()