"""
דור שמו 207932740
יובל רוטברג 211877592
"""
#function definition for finding the perfect number.
"""conduct a survey and check which media is the most effective for advertising a new construction plan"""
#comment: main function - start point
def main():
    #initialize counter
    radio, tv, social_media, flyers = 0,0,0,0
    #get input from user
    ch = input(" Enter answers(R-radio, T-tv, S-social media, F-flyers, * to end)\n")
    #loop until user enters '*'
    while ch != '*' :
        #check user response and increment the corresponding counter
        if ch == 'R':
            radio += 1
        elif ch == 'T':
             tv += 1
        elif ch == 'S':
             social_media += 1
        elif ch == 'F':
              flyers += 1  
        else:
        #print error message if input is invalid
              print("Illegal input:" ,ch)
        #input to read another response from the user
        ch = input()
    #determine the most popular type of advertising and print the result
    if flyers >= radio and flyers >= tv and flyers >= social_media :
        print("Survey results: The best advertising strategy is: (F)")
    elif radio >= social_media and radio >= tv :
        print("Survey results: The best advertising strategy is: (R)")
    elif social_media >= tv :
            print("Survey results: The best advertising strategy is: (S)")
    else :  print("Survey results: The best advertising strategy is: (T)")
#start the program
main()