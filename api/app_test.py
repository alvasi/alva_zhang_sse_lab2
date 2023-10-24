# from app import process_query


# def test_knows_about_dinosaurs():
#     assert (
#         process_query("dinosaurs") ==
#         "Dinosaurs ruled the Earth 200 million years ago"
#     )


# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"

from app import handle_guess


def test_handle_guess_lower():
    result = handle_guess(1)
    assert result.startswith("Too low!. Number of remaining guesses is")

def test_handle_guess_higher():
    result = handle_guess(100)
    assert result.startswith("Too high!. Number of remaining guesses is")

def test_handle_guess_correct():
    for i in range(101):  # assuming the secret number is between 0 and 100
        result = handle_guess(i)
        if result == "Correct!":
            break
    else:
        assert False, "The secret number was not found"

def test_handle_guess_invalid():
    assert handle_guess("abc") == "Invalid query. Please enter a number."

def test_handle_guess_no_remaining_guesses():
    for _ in range(8):  # assuming the maximum number of guesses is 7
        result = handle_guess(100)  # always guess a number that is too high
    assert result == "Unlucky! No remaining guesses."
