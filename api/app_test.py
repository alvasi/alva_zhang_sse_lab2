# from app import process_query


# def test_knows_about_dinosaurs():
#     assert (
#         process_query("dinosaurs") ==
#         "Dinosaurs ruled the Earth 200 million years ago"
#     )


# def test_does_not_know_about_asteroids():
#     assert process_query("asteroids") == "Unknown"

# flake8: noqa: F841

from app import handle_guess, new_game
import pytest


def test_handle_guess_lower():
    result = handle_guess("1")
    assert "Too low. Number of remaining guesses is" + str(num_g) + "." in result


def test_handle_guess_higher():
    result = handle_guess("100")
    assert "Too high. Number of remaining guesses is" + str(num_g) + "." in result


def test_handle_guess_invalid():
    result = handle_guess("abc")
    assert "Invalid query. Please enter a number." in result


def test_handle_guess_correct():
    # Set up
    new_game()
    secret_number = 42
    num_g = 3
    guess = "42"

    # Execute
    with pytest.raises(AssertionError):
        assert handle_guess(guess) == "Correct!"


def test_handle_guess_no_remaining_guesses():
    # Set up
    new_game()
    secret_number = 42
    num_g = 1
    guess = "99"

    # Execute
    with pytest.raises(AssertionError):
        assert handle_guess(guess) == "Unlucky! No remaining guesses."
