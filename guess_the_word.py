# Omar Oregon
# CIS256 Term Year Fall 2026
# Programming Assignment 4

# imorted libraries
import random 

# create word list
word_list = ["apple", "tiger", "house", "chair", "beach",
    "planet", "forest", "puzzle", "rocket", "garden", "diamond",
    "journey", "penguin", "library", "monster", "computer", "elephant",
    "mountain", "dinosaur", "umbrella", "algorithm", "adventure",
    "chocolate", "pineapple", "knowledge", "astronaut", "mysterious",
    "jellyfish", "microscope", "programming"]

# Implement the game guess this word

# Select a random word from the word_list 
def choose_random_word(word_list):
    random_word = random.choice(word_list)
    return random_word

# a function that prompts the user to guess one letter at a time
def player_guess():
    while True:
        guess = input("Please guess a letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            return guess
        elif len(guess) > 1:
            print("Please only enter one letter at a time")
        elif not guess.isalpha():
            print("Please only enter one letter")
            
# a function that reveal letters when the user guesses correctly
def verify_guess(random_word, guess):
    my_guess = guess in random_word
    return my_guess

# a function that checks if a letter appears more than once in the word, reveal all instances of that letter
def reveal_letters_guessed(random_word, guess_list):
    for letter in random_word:
        if letter in guess_list:
            print(letter, end = " ")
        else:
            print("_", end = " ")
    print()         

# function allow letters to be guessed in any order and reveal correct guesses immediately
# allows the user to continue until the user guesses the word or runs out of attempts
# display a congratulatory message when the word is successfully guessed
def start_game():
    chosen_word = choose_random_word(word_list)
    guess_list = []
    player_attempts = 7
    
    print("Welcome to guess that word!")
    
    while player_attempts > 0:
        print("Lets play guess that word")
        guess = player_guess()
        
        if guess not in guess_list:
            guess_list.append(guess)
        else:
            print("You already guessed this letter: ", guess)
            continue
        
        review_letter = verify_guess(chosen_word, guess)
        
        if review_letter:
            print("Correct guess", guess)
        else:
            print("please try again!")
            player_attempts -= 1
            print(f"You have {player_attempts} attempts left ")
        
        reveal_letters_guessed(chosen_word, guess_list)
        
        correct_result = all(char in guess_list for char in chosen_word)
        if correct_result:
            print("Congardulations you successfully guesed the word: ", chosen_word)
            break
        elif player_attempts == 0:
            print("Nice try, you have reached your max attempts")
        else:
            continue
            
# The main program, prevents the unit test from running the whole program 
if __name__ == "__main__":               
    start_game()


