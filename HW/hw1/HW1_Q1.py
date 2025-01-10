
def main():
# creating input for the first letter in every strategy    
    print("Enter answers(R-radio, T-tv, S- social media,F-flyers, * to end)")
    answer = input()
# creating variebles that equal to 0 to collect the votes
# max is for the one with the most votes and best strategy is for the leeter with the most votes.
    radio = 0
    tv = 0
    flyers = 0
    social = 0
    Max = 0
    best_strategy = ''
#creating a loop to find the best strategy
    while answer != '*':
# first if statement to seperate each strategy abd for every vote plus one for his varieble.
        if answer == 'F':
            flyers += 1
# secend if statement to find out the max strategy and if he's max then store it in max.
            if flyers >= Max:
              Max = flyers
# statement for in case two or more strategy as the same number of vote, to best strategy will be chosen base on the ABC order.          
              if (flyers >= social) and (flyers >= tv) and (flyers >= radio):
                    best_strategy = '(F)'
        elif answer == 'S':
            social += 1
            if social >= Max:
                if (social > flyers) and (social >= tv) and (social >= radio):
                    best_strategy = '(S)' 
        elif answer == 'T':
            tv += 1
            if tv >= Max:
                Max = tv
                if (tv > social) and (tv > flyers) and (tv >= radio):
                    best_strategy = '(T)'
        elif answer == 'R':
            radio += 1
            if radio >= Max:
                Max = radio
                if (radio > social) and (radio > flyers) and (radio > flyers):
                    best_strategy = '(R)'
        else:
# in case of diffrent letter than the 4 we want, printing illegal input.
            print("Illegal input:",answer)
        answer = input()
#print the sesult of the survey.
    print("Survey results :The best advertising strategy is:",best_strategy)
    
main()
