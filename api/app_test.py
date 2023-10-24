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
from unittest.mock import patch
from app import app


def test_handle_guess_lower():
    result = handle_guess(1)
    assert result.startswith("Too low!. Number of remaining guesses is")


def test_handle_guess_higher():
    result = handle_guess(100)
    assert result.startswith("Too high!. Number of remaining guesses is")


def test_handle_guess_invalid():
    assert handle_guess("abc") == "Invalid query. Please enter a number."


def set_globals_correct():
    global secret_number, num_g
    secret_number = 60
    num_g = 4


def test_query_correct():
    with patch('app.new_game') as mock_new_game:
        mock_new_game.return_value = "Correct!"
        mock_new_game.side_effect = set_globals_correct
        with app.app_context():
            result = query("60")
        assert "Correct!" in result


def set_globals_no_guesses():
    global secret_number, num_g
    secret_number = 60
    num_g = 1


def test_query_no_remaining_guesses():
    with patch('app.new_game') as mock_new_game:
        mock_new_game.return_value = "Unlucky! No remaining guesses."
        mock_new_game.side_effect = set_globals_no_guesses
        with app.app_context():
            result = query("100")
        assert "Unlucky! No remaining guesses." in result
