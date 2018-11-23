# Simple dice rolling simulator 
from random import randint

def die_roll():
    return randint(1, 6)

# def roll_again():
#     roll_request = raw_input("Roll the die? [y/n] ")
#     answer = roll_request.lower()
#     if answer == "yes" or answer == "y":
#         print die_roll()
#         roll_again()
#     elif answer == "no" or answer == "n":
#         print "Thank you for rolling!"
#     else:
#         print "Sorry, I did not recognize that answer"
#         roll_again()
        
# print roll_again()

# Multiple dice option
def roll_dice():
    roll_request = raw_input("Roll the die? [y/n] ")
    answer = roll_request.lower()
    if answer == "yes" or answer == "y":
        num_of_rolls = int(raw_input("You can roll up to 5 dice at a time, how many would you like to roll? "))
        if num_of_rolls > 5 or num_of_rolls < 1:
            print "Please choose a number between 1 and 5"
            roll_dice()
        else:
            i = 1
            while i <= num_of_rolls:
                print die_roll()
                i += 1
            roll_dice()
    elif answer == "no" or answer == "n":
        print "Thank you for rolling!"
    else:
        print "Sorry, I did not recognize that answer"
        roll_dice()

print roll_dice()