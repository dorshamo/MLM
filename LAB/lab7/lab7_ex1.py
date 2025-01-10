#1.Enter integer:
#Enter x:
#Original list: 
#New list: 
""" function to create a list"""
def input_list(n):
    lst = []
    count = 1
    while n > 0:
        print(count,".",sep='',end='')
        num = int(input("Enter integer: "))
        count +=1
        n-=1
        lst.append(num)
    return lst
""" function to create the new list"""
#the function takes the old list and the nmber we input and checks for the numbers the smaller and bigger then x and puts them in order
def create_new_list(lst,x):
    new_lst = []
    temp_lst = []
    for i in lst:
        if i < x:
            new_lst.append(i)
        else:
            temp_lst.append(i)
    new_lst+=temp_lst
    return new_lst
""" main function to input x and call the functions"""
def main():
    lst = input_list(7)
    x = int(input("Enter x: "))
    new_lst = create_new_list(lst,x)
    print("Original list:",lst)
    print("New list:",new_lst)
main()
