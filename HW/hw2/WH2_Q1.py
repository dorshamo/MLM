
import math
import random



def who_starts(A,B):
    """
    decide which player starts the game randomly.
    
    Parameters
    ----------
    A : int
       the starting position of player A.
    B : int
       the starting position of player B.

    Returns
    -------
    str
        a string indicating which player starts the game.
    
    """
    while A == B:
        A = random.randrange(1,7)
        B = random.randrange(1,7)
    if A > B:
        return 'A'
    else:
        return 'B'
    


def is_prime(n):
    """
    check if a number is prime.
    
    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    bool
        True if the number is prime, False otherwise.

    """
    i = 3
    if n!=2 and n%2==0:
        return False
    else: 
        limit = math.sqrt(n)
        while i <=limit:
            if n%i ==0:
                return False
            i +=2
        return True
    
    
    
def equal_digits(n):
    """
    check if the tens digit is equal to the units digit in a given two-digit number.
    
    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    bool
        True if the tens digit is equal to the units digit, False otherwise.

    """
    if n%10 == n //10 and n<55:
        return True
    return False



def perfect_square(n):
    """
    check if a number is a perfect square.
    
    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    bool
        True if the number is a perfect square, False otherwise.

    """
    if math.sqrt(n) % 1 != 0:
        return False
    return True



def sum_digits(n):
    """
    check the sum of the two digits of the number.
    
    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    sum_dig : int
        return the sum of the digits.

    """
    sum_dig = 0
    sum_dig+= n%10
    sum_dig+= n//10
    return sum_dig



def is_ladder(n):
    """
    check if a number represents a ladder.

    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    bool
        True if the number represents a ladder, False otherwise.

    """
    sum_dig = sum_digits(n)
    if is_prime(sum_dig):
        return True
    elif equal_digits(n):
        return True
    return False



def is_rope(n):
    """
    check if a number represents a rope.

    Parameters
    ----------
    n : int
        the number to be checked.

    Returns
    -------
    bool
        True if the number represents a rope, False otherwise.

    """
    if is_prime(n):
        return True
    elif perfect_square(n):
        return True
    return False



def scorenew(n):
    """
    checks the new score after the modes.
    
    Parameters
    ----------
    n : int
       the original score.


    Returns
    -------
    n : int
       The adjusted score after applying  conditions

    """
    if is_ladder(n) and is_rope(n):
        return n - 5
    elif is_rope(n):
        return n - 5
    elif is_ladder(n):
        return n + 10
    else:
        return n
  
    
  
""" main function to create the game """      
def main():
    A = 0
    score1 = 0
    B = 0
    score2 = 0
#print to show that the game start and choseing the the first player with the rolling die function.
    print('The game "ladders and ropes" starts!')
    first_name = who_starts(A, B)
#if statement for the name of the first and the second player.
    if first_name == 'A':
      second_name = 'B'
    else:
        second_name = 'A'  
    first = 0
    second = 0    
#printing the player that start.
    print("Player",first_name,"opens the game.")
#while loop to end the game when one of the players gets to 50 points.
    while score1 < 50 and score2 <50:
#inner loop creats turns inside the loop for each player end to stop the loop when 1 of them get to 50 points.
        while first == 0 and score2<50:
#roling a die each turn and sum the points, after that cheking the mode of the score.
            first = random.randrange(1,7)
            score1+=first
            score1 = scorenew(score1)
#if the score under zero reset the score and go to the next player.
            if score1 < 0:
                score1 = 0
#printing the score every round.
            print("Player",first_name,":    die roll:",first,"    total points:",score1)
#same things we did to the first plater we do to the second one.
        while second == 0 and score1<50:
            second = random.randrange(1,7)
            score2+=second
            score2 = scorenew(score2)
            if score2 < 0:
                score2 = 0
            print("Player",second_name,":    die roll:",second,"    total points:",score2)
        first = 0
        second = 0
#printing the name of the winner of the game.
    if score1 >=50:
        print("The winner is: player",first_name,"!!!")
    else:
        print("The winner is: player",second_name,"!!!")
main()
