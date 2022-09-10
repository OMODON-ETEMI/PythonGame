import random 
# creating a hangman a game
from game.word import words
import string
def get_a_word(x):
    word = random.choice(words) # tells the computer to randomly pick a word from the list
    while '-' in word or ' ' in word:
        word = random.choice
    return word.upper()
def hangman():
    word = get_a_word(words) #calling the get a word function
    guessed_word = set(word) #converting it into a set 
    alphabet = set(string.ascii_uppercase) #create a set of alphabets in capital letters
    used_letter = set() # letters used by user
    lives = 6
    while len(guessed_word) > 0 and lives > 0:
        letter = input(f'you have {lives} lives left \nGuess a letter: ').upper()
        if letter in used_letter:
            print('You have guessed this letter before guess again')
        else:
            if letter in alphabet:
                used_letter.add(letter)
                print('Letters used so far are: ',' '.join(used_letter))
                if letter in word:
                    print('You guessed correctly')
                    guessed_word.remove(letter)
                else:
                    print('you guessed wrong')
                    lives = lives - 1
            else:
                print('invalid syntax guess again')
            answer = [letters if letters in used_letter else '_' for letters in word]
            print('current word: ',' '.join(answer))
    if lives > 0:
        print('Yay!! you have won')
    else:
        print('Sorry!! but you lost')
hangman()
