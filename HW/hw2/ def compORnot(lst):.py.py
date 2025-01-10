
""" function to find if the list is compressable or not"""
def compORnot(lst):
    if lst.count(0) > (len(lst)/2): 
        return True
    else:
        return False
#return if true or false



""" function to find the compressed list"""
def compressed(lst):
    compressed_lst = []
    zero_count = 0
    compressed_lst.append(lst[0])
    for g in range(2,len(lst)):
        if lst[g] > 0:
            compressed_lst.append(zero_count)
            compressed_lst.append(lst[g])
            zero_count = 0
        elif lst[g] == 0:
            zero_count += 1
    compressed_lst.append(zero_count)
    return compressed_lst
#return the compressed list.



""" function to find the uncompressed list by using the compressed list"""
def uncompressed(compressed_lst):
    uncompressed_lst = []
    for i in range(len(compressed_lst)):
        if i % 2 == 0:
            uncompressed_lst.append(compressed_lst[i])
        else:
            uncompressed_lst += [0] * compressed_lst[i]
    return uncompressed_lst
#return the uncompressed list.
            
            
""" main function to ask the user for numbers for the list with the last one -1 to stop the loop"""  
def main():
    print("Please enter list of numbers, end with -1: ")
    num = int(input())
    lst =[]
    while num != -1:
        lst.append(num)
        num = int(input())
#if statement for the two options (compressable or not), with there print masseges.
    if compORnot(lst):
        compressed_lst = compressed(lst)
        uncompressed_lst = uncompressed(compressed_lst)
        print("The list is compressable.")
        print("The compressed list is:",compressed_lst)
        print("The uncompressed list is:",uncompressed_lst)
    else:
        print("The list is not compressable.")
main()
#calling for main


    
