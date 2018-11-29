import random

categories = {
    "animal": ["alpaca", "chinchilla", "dolphin", "orca", "rabbit"],
    "country": ["canada", "namibia", "peru", "switzerland", "taiwan"],
    "fruit": ["cherry", "kiwi", "mango", "papaya", "strawberry"],
    "game": ["chess", "monopoly", "operation", "risk", "scrabble"],
    "movie": ["casablanca", "frozen", "inception", "jaws", "titanic"]
}

# user_choice = raw_input("Please choose a category: ")
# user_category = categories[user_choice]
# hidden_word = random.choice(user_category)
# print hidden_word
# print "*" * len(hidden_word)



def hangman():
    print "Hello! Welcome to Python Hangman! There are five categories of words: animal, country, fruit, game, and movie."
    user_choice = raw_input("To get started, please choose one of the available categories: ")
    if user_choice.lower() in categories.keys():
        user_category = categories[user_choice.lower()]
        hidden_word = random.choice(user_category)
        guessed_letters = []
        incorrect_guesses = 6
        print hidden_word
        while incorrect_guesses > 0:
            user_guess = raw_input("Please guess a letter: ")
            letter_guess = user_guess.lower()
            if len(letter_guess) == 1:
                if letter_guess.isalpha():
                    guessed_letters.append(letter_guess)
                    guessed_letters.sort()
                    print "Guessed letters: " , guessed_letters
                    if letter_guess in hidden_word:
                        print letter_guess
                    else:
                        incorrect_guesses -= 1
                        print "Sorry, that letter is not in the word. You have " + str(incorrect_guesses) + " incorrect guesses remaining."
                else:
                    print "That is not a letter, please guess only letters"
            else:
                print "Please guess only one letter"
    else:
        print "Sorry that is not one of the categories"
        hangman()

print hangman()
