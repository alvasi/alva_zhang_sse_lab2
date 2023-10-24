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
    assert handle_guess("50") == "Too low!. Number of remaining guesses is 6."


def test_handle_guess_higher():
    assert handle_guess("70") == "Too high!. Number of remaining guesses is 5."


def test_handle_guess_correct():
    assert handle_guess("60") == "Correct!"


def test_handle_guess_invalid():
    assert handle_guess("abc") == "Invalid query. Please enter a number."


def test_handle_guess_no_remaining_guesses():
    assert handle_guess("80") == "Unlucky! No remaining guesses."
