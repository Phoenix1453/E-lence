import random

def select_random_word(category):
    with open(category + '.txt', 'r') as f:
        words = f.read().splitlines()
    return random.choice(words)

def select_category():
    categories = ['meyve', 'şehir', 'eşya']
    return random.choice(categories)

used_words = []
while True:
    play_again = input("Tekrar oynamak ister misiniz? (e/h) ")
    if play_again.lower() == 'h':
        print("İyi oyundu!")
        break
    category = select_category()
    if category == 'meyve':
        print("Bu kelime bir meyvedir.")
    elif category == 'şehir':
        print("Bu kelime bir şehirdir.")
    else:
        print("Bu kelime bir eşyadır.")
    word = select_random_word(category)
    used_words.append(word)
    hidden_word = ['_'] * len(word)
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    used_letters = []
    while True:
        print(' '.join(hidden_word))
        guess = input("Bir harf tahmin edin: ")
        if len(guess) != 1:
            print("Lütfen sadece bir harf tahmin edin.")
        elif guess in used_letters:
            print("Bu harfi daha önce kullandınız. Lütfen farklı bir harf tahmin edin.")
        elif not guess.isalpha():
            print("Lütfen sadece harf tahmin edin.")
        else:
            used_letters.append(guess)
            if guess.lower() in word:
                print("Doğru tahmin! Kelime içinde bu harf var.")
                for i in range(len(word)):
                    if word[i] == guess.lower():
                        hidden_word[i] = guess.lower()
                if '_' not in hidden_word:
                    print("Tebrikler, kelimeyi buldunuz: " + word)
                    break
            else:
                print("Yanlış tahmin! Kelime içinde bu harf yok.")
                incorrect_guesses += 1
                if incorrect_guesses == max_incorrect_guesses:
                    print("Maksimum yanlış tahmin sayısına ulaştınız. Kelime: " + word)
                    break
