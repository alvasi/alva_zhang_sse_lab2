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
    assert "Too low. Number of remaining guesses is" in result


def test_handle_guess_higher():
    result = handle_guess("100")
    assert "Too high. Number of remaining guesses is" in result


def test_handle_guess_invalid():
    result = handle_guess("abc")
    assert "Invalid query. Please enter a number." in result


@pytest.fixture(scope="session")
def global_variables_correct():
    secret_number = 42
    num_g = 3
    return secret_number, num_g


def test_handle_guess_correct(global_variables_correct):
    # Set up
    secret_number, num_g = global_variables_correct
    result = handle_guess("42")
    assert "Correct!" in result


@pytest.fixture(scope="session")
def global_variables_no_remain():
    secret_number = 42
    num_g = 1
    return secret_number, num_g


def test_handle_guess_no_remain(global_variables_no_remain):
    # Set up
    secret_number, num_g = global_variables_no_remain
    result = handle_guess("99")
    assert "Unlucky! No remaining guesses." in result
