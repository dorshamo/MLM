"""
Multi Line comments...

File name: lab4_q1.py
Description: ...
"""

#single line comment
def main():
#creating input for weight and height 
   weight = int(input("Enter weight (in kg): "))
   height = int(input("Enter height (in cm): "))
   height_m =height/100
#calculating the bmi with the height and weight
   BMI = weight / (height_m**2)
   #using if statemant to show in what category the bmi that we got
   if BMI<18.5:
       print("Underweight")
   elif BMI<25.0 and 18.5<=BMI:
       print("Normal weight")
   elif BMI<30.0 and 25.0<=BMI:
       print("Increased weight")
   elif BMI<40.0 and 30.0<=BMI:
       print("Obese")
   elif BMI>=40.0:
       print("Very high obese")
     
main()