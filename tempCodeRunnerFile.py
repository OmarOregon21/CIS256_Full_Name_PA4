# assert that guess is not in chosen word
def test_is_guess_not_in_word():
    temp_string = "topic"
    my_guess = "f"   
    verify = verify_guess(temp_string, my_guess)
    assert verify is False