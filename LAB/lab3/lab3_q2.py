
def main():
    #make an input to enter a number
    x = float(input("Please insert x: "))
    #calculate the new number
    new_x = x+(x**(1/3)+x**2)**(1/2)
    print('%.2f'%x,'+(','%.2f'%x,'^(1/3)+','%.2f'%x,'^2)^0.5=','%.2f'%new_x,sep="")

main()
