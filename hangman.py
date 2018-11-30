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
# letter_list = list(hidden_word)
# hidden_letters = []
# for i in hidden_word:
#     hidden_letters.append("-")
# print hidden_letters
# fill_in = "".join(hidden_letters)
# user_guess = raw_input("Please guess a letter: ")
# letter_guess = user_guess.lower()
# if user_guess in hidden_word:
#     letter_search = [i for i, e in enumerate(letter_list) if e == letter_guess]
#     for i in letter_search:
#         hidden_letters[i] = user_guess
#     print hidden_letters
#     print "".join(hidden_letters)

def hangman():
    print "Hello! Welcome to Python Hangman! There are five categories of words: animal, country, fruit, game, and movie."
    user_choice = raw_input("To get started, please choose one of the available categories: ")
    if user_choice.lower() in categories.keys():
        user_category = categories[user_choice.lower()]
        guess_word = random.choice(user_category)
        # Turn guess_word into list form to be able to get index of guessed letters if in guess_word
        word_as_list = list(guess_word)

        # Output so users can see num of letters in guess_word
        word_as_blanks = []
        for i in guess_word:
            word_as_blanks.append("-")
        # Print word_as_blanks as str
        fill_in_blank = "".join(word_as_blanks)
        
        guessed_letters = []
        incorrect_guesses = 6

        print guess_word
        print fill_in_blank

        while incorrect_guesses > 0:
            user_guess = raw_input("Please guess a letter: ")
            letter_guess = user_guess.lower()
            if len(letter_guess) == 1 and letter_guess.isalpha() and letter_guess not in guessed_letters:
                guessed_letters.append(letter_guess)
                guessed_letters.sort()
                print "Guessed letters: " , guessed_letters
                if letter_guess in guess_word:
                    # List comprehension for search for indexes of correct letter guess in guess_word
                    letter_index_search = [i for i, char in enumerate(word_as_list) if char == letter_guess]
                    
                    # Replace appropriate "-" with correctly guessed letter
                    for i in letter_index_search:
                        word_as_blanks[i] = letter_guess
                    print "".join(word_as_blanks)
                else:
                    incorrect_guesses -= 1
                    print "Sorry, that letter is not in the word. You have " + str(incorrect_guesses) + " incorrect guesses remaining."
            elif len(letter_guess) != 1:
                print "Please guess only one letter"
            elif letter_guess.isalpha() == False:
                print "That is not a letter, please guess only letters"
            elif letter_guess in guessed_letters:
                print "You guessed that letter already!"
                print "You have " + str(incorrect_guesses) + " incorrect guesses remaining."
        print "Sorry, game over! Your word was: %s" % (guess_word)
    else:
        print "Sorry that is not one of the categories"
        hangman()

print hangman()
