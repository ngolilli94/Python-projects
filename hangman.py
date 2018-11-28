import random

categories = {
    "animals": ["alpaca", "chinchilla", "dolphin", "orca", "rabbit"],
    "countries": ["canada", "namibia", "peru", "switzerland", "taiwan"],
    "fruits": ["cherry", "kiwi", "mango", "papaya", "strawberry"],
    "games": ["chess", "monopoly", "operation", "risk", "scrabble"],
    "movies": ["casablanca", "frozen", "inception", "jaws", "titanic"]
}

# user_choice = raw_input("Please choose a category: ")
# user_category = categories[user_choice]
# hidden_word = random.choice(user_category)
# print hidden_word
# print "_ " * len(hidden_word)



def hangman():
    print "Hello! Welcome to Python Hangman! There are five categories of words: animals, countries, fruits, games, and movies."
    user_choice = raw_input("To get started, please choose one of the available categories: ")
    if user_choice.lower() in categories.keys():
        user_category = categories[user_choice]
        hidden_word = random.choice(user_category)
        guessed_letters = []
        
    else:
        print "Sorry that is not one of the categories"
        hangman()

print hangman()
