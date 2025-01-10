def main():
    #create an input to enter a triangle sides
   a,b,c =  eval(input("Please insert triangle sides: "))
   print('a = ','%.1f'%a,', b = ','%.1f'%b,', c = ','%.1f'%c,sep='')
   perimeter = a+b+c
   perimeter_2 = perimeter/2
   print("perimeter =","%.3f"%perimeter)
   #set a variable that contains the Heron's formula with the numbers and the parimeter/2
   area = (perimeter_2*(perimeter_2-a)*(perimeter_2-b)*(perimeter_2-c))**(1/2)
   #print the answer
   print("Area =","%.3f"%area)
main()
