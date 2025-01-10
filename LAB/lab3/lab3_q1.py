#the program gets numbers and calculates the square and the cube of them
def main():
    num = int(input("Enter number: "))
    num_1 = num +1
    num_2 = num_1 +1
    num_3 = num_2 +1
    num_4 = num_3 +1
    num_a = num**2
    num_b = num**3
    num_1a = num_1**2
    num_1b = num_1**3
    num_2a = num_2**2
    num_2b = num_2**3
    num_3a = num_3**2
    num_3b = num_3**3
    num_4a = num_4**2
    num_4b = num_4**3
    #speces between the strings
    print("number","square","cube",sep='        ')
    #spaces between integers
    print("%3d"%num,"%14d"%num_a,"%14d"%num_b)
    print("%3d"%num_1,"%14d"%num_1a,"%14d"%num_1b)
    print("%3d"%num_2,"%14d"%num_2a,"%14d"%num_2b)
    print("%3d"%num_3,"%14d"%num_3a,"%14d"%num_3b)
    print("%3d"%num_4,"%14d"%num_4a,"%14d"%num_4b)
main()

