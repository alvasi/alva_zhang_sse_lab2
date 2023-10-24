# from app import process_query


# def test_knows_about_dinosaurs():
#     assert (
#         process_query("dinosaurs") ==
#         "Dinosaurs ruled the Earth 200 million years ago"
#     )


# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"

from app import handle_guess
from app import query


def test_handle_guess_lower():
    result = handle_guess(1)
    assert result.startswith("Too low!. Number of remaining guesses is")


def test_handle_guess_higher():
    result = handle_guess(100)
    assert result.startswith("Too high!. Number of remaining guesses is")


def test_query_correct():
    global secret_number
    secret_number = 60
    result = query(60)
    assert result.startswith("Correct!")


def test_handle_guess_invalid():
    assert handle_guess("abc") == "Invalid query. Please enter a number."


def test_query_no_remaining_guesses():
    global num_g secret_number
    num_g = 1
    secret_number = 60
    result = query(100)
    assert result.startswith("Unlucky! No remaining guesses.")
