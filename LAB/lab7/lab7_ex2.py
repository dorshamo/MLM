#Enter number of runners:
#Time average is 17.53.
#The number of runners, running below average time is 4
"""function to find the average running time with the list of times"""
def my_avg(time_lst):
    sum = 0
    for i in time_lst:
        sum+=i
    avg = sum/len(time_lst)
    return avg

"""main function to create the input for the amount of runners and the list of times"""
def main():
    runners = int(input("Enter number of runners: "))
    time_lst = []
    below_avg_sum = 0
    count = 1
    while runners >0:
        print(count,".",sep='',end='')
        time = float(input("Enter time: "))
        time_lst.append(time)
        runners-=1
        count+=1
#finding how many runners are below average.
    avg = my_avg(time_lst)
    for i in time_lst:
        if i < avg:
            below_avg_sum+=1
    print("Time average is ","%.2f"%avg,'.',sep='')
    print("The number of runners, running below average time is ",below_avg_sum,'.',sep='')
main()

