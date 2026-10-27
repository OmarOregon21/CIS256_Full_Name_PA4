# Omar Oregon
# CIS256 Term Year Fall 2026
# Programming Assignment 4

import pytest

from guess_the_word import choose_random_word, player_guess, verify_guess, reveal_letters_guessed, start_game

#Write tests that check:
#       The selected word comes from the predefined list.
#       Guesses are processed correctly, including correct and incorrect guesses.

# assert that a word is in the list
def test_chose_randomly():
    temp_list = ["orange", "bat", "cat"]
    word = choose_random_word(temp_list)
    assert word in temp_list

# asert play guess.
#def test_check_player_guess():
 #   player_guess()
            
# assert that guess is in chosen word
def test_is_guess_in_word():
    temp_string = "help"
    my_guess = "h"
    assert verify_guess(temp_string, my_guess)

# assert that guess is not in chosen word
def test_is_guess_not_in_word():
    temp_string = "topic"
    my_guess = "f"   
    verify = verify_guess(temp_string, my_guess)
    assert verify is False
     


