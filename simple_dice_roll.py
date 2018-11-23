# Simple dice rolling simulator 
from random import randint

def die_roll():
    return randint(1, 6)

def roll_again():
    roll_request = raw_input("Roll the die? [y/n] ")
    answer = roll_request.lower()
    if answer == "yes" or answer == "y":
        print die_roll()
        roll_again()
    elif answer == "no" or answer == "n":
        print "Thank you for rolling!"
    else:
        print "Sorry, I did not recognize that answer"
        roll_again()
        
print roll_again()