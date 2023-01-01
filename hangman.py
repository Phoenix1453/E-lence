import random

def select_random_word(category):
    with open(category + '.txt', 'r') as f:
        words = f.read().splitlines()
    return random.choice(words)

def select_category():
    categories = ['fruit', 'city', 'object']
    return random.choice(categories)

used_words = []
while True:
    play_again = input("Would you like to play? (y/n) ")
    if play_again.lower() == 'n':
        print("Goodbye!")
        break
    category = select_category()
    if category == 'fruit':
        print("This word is a fruit.")
    elif category == 'city':
        print("This word is a city.")
    else:
        print("This word is an object.")
    word = select_random_word(category)
    used_words.append(word)
    hidden_word = ['_'] * len(word)
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    used_letters = []
    while True:
        print(' '.join(hidden_word))
        guess = input("Guess a letter: ")
        if len(guess) != 1:
            print("Please enter only one letter.")
        elif guess in used_letters:
            print("You have already used this letter. Please enter a different letter.")
        elif not guess.isalpha():
            print("Please enter only a letter.")
        else:
            used_letters.append(guess)
            if guess.lower() in word:
                print("Correct guess! This letter is in the word.")
                for i in range(len(word)):
                    if word[i] == guess.lower():
                        hidden_word[i] = guess.lower()
                if '_' not in hidden_word:
                    print("Congratulations, you have found the word: " + word)
                    break
            else:
                print("Incorrect guess! This letter is not in the word.")
                incorrect_guesses += 1
                if incorrect_guesses == max_incorrect_guesses:
                    print("You have reached the maximum number of incorrect guesses. The word was: " + word)
                    break
