def is_letter(test_subject):
    if(len(test_subject) != 1):
        return False

    if(test_subject >= 'a' and test_subject <= 'z'):
        return True
    elif(test_subject >= 'A' and test_subject <= 'Z'): # hangman is played with small letters
        new_letter = chr(test_subject) + (ord('a') - ord('A'))
        test_subject = new_letter
        return True
    else:
        return False

def draw_hangman(hangman, mistakes):
    print("_________")
    print("|     |")
    
    if(mistakes > 0):
        print("|    ", end="")
        print(hangman[0])
    else:
        print("|    ")

    if(mistakes > 1):
        print("|    ", end="")
        if(mistakes == 2):
            print(hangman[2])
        else:
            print(hangman[2], end="")
            if(mistakes == 3):
                print(hangman[1])
            else:
                print(hangman[1], end="")
                print(hangman[3])
    else:
        print("|    ")

    if(mistakes > 4):
        print("|    ", end="")
        if(mistakes == 5):
            print(hangman[4])
        else:
            print(hangman[4], end="")
            print(hangman[5])
    else:
        print("|    ")
              
    print("|    ")
    print("--")

def hangman_game(word_to_guess):
    hangman = [" O", "|", "/", "\\", " |", "\\"]
            # _________
            # |     O
            # |    /|\
            # |     |\
            # |
            # --
    
    draw_hangman(hangman, 0) # drawing the empty post, before the game starts
    game_ongoing = True
    mistakes = 0
    guess_so_far = ["_"] * len(word_to_guess)

    while(game_ongoing):
        tries_left = len(hangman) - mistakes - 1
        if(tries_left < 0 or guess_so_far == word_to_guess):
            game_ongoing = False
            break

        letter_guessed = input("Enter a guess (one letter): ")
        while(is_letter(letter_guessed) == False):
            letter_guessed = input("Enter a guess (one letter): ")

        if(letter_guessed in guess_so_far):
            print("You already tried this letter!")
        else:
            if(letter_guessed not in word_to_guess):
                mistakes += 1
                draw_hangman(hangman, mistakes)
            else:
                # guess_so_far[word_to_guess.find(letter_guessed)] = letter_guessed # only works if letter is unique
                indexes = [i for i, val in enumerate(word_to_guess) if val == letter_guessed]
                for i in indexes:
                    guess_so_far[i] = letter_guessed
            print(" ".join(guess_so_far)) # prints list like it would print a string (just spaces in between elements)

            if(guess_so_far == word_to_guess):
                game_ongoing = False
            else:
                print("Tries left:", tries_left)
                if(tries_left == 0):
                    print("You lost")
                    game_ongoing = False

# choosing a word to guess from a text file
import random
from pathlib import Path
import re

# root_dfirst_letter + word_to_guess[slice(1, len(word_to_guess))] # add the rest of the word to the now lowercase letter
root_dir = Path(__file__).parent
text_file = root_dir / "bee_movie_script.txt"
# print(text_file.read_text()) # prints the whole text
word_to_guess = random.choice(open(text_file).readline().split()) #splits with empty characters as separators => gets a word
word_to_guess = re.split(r'[\\;:-_,!`~/\"\',.?\s\n]+', word_to_guess) #removes any punctuation marks

while(len(word_to_guess) < 4): 
    # valid word (lenght > 0) and harder to guess
    word_to_guess = random.choice(open(text_file).readline().split())
    word_to_guess = re.split(r'[\\;:-_,!`~/\"\',.?\s\n]+', word_to_guess)[0]

word_to_guess = str(word_to_guess)

if(word_to_guess[0] < 'a'): #if the word starts with a capital letter
    first_letter = chr(ord(word_to_guess[0]) + (ord('a') - ord('A')))  #write it in lowercase
    word_to_guess = first_letter + word_to_guess[slice(1, len(word_to_guess))] # add the rest of the word to the now lowercase letter

# playing hangman
hangman_game(word_to_guess)
