def main():
#creating input for th first element,the quotient and the index/position of the sequence.
    a_1 = int(input("Enter the first element in a geometric sequence: "))
    q = int(input("Enter the quotient of a geometric sequence: "))
    n = int(input("Enter an index / position in a sequence - a natural number: "))
#varieble to store the new number of the sequence.
    a_n = a_1
    print("The first",n,"elements in the sequence are: ")
#creating loop to find all the elements of the sequence by muliply inside the loop the first element with the quotient. 
    for i in range(1,n+1):
#printing the elements.
        print(a_n,end=' ')
        a_n *=q




main()