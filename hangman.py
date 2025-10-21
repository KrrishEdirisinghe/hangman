import random
from words import words
import string

def computer_choose():
    return random.choice(words)

def display_word():
    computer = computer_choose()
    word_letters = set(computer)
    used_letters = set()
    lives = 6
    print('welcome to my hangman game')
    while len(word_letters) > 0 and lives > 0:
        DISPLAY = [letter if letter in used_letters else '-' for letter in computer]
        print(f'lives : {lives} \n {" ".join(DISPLAY)}')
        
        guess = input('guess a letter ').lower()
        
        if guess in word_letters:
            used_letters.add(guess)
            word_letters.remove(guess)
            
 
        elif guess in used_letters:
            print('you already guessed that')

        else:
            used_letters.add(guess)
            lives = lives - 1
            print('INCORRECT')
    if lives == 0:
        print(f'you died \nthe word was {computer}' )
    else:         
        print(f'you win! \nthe word was {computer}')
display_word()



