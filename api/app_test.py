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
    result = handle_guess("1")
    assert "Too low. Number of remaining guesses is" in result


def test_handle_guess_higher():
    result = handle_guess("100")
    assert "Too high. Number of remaining guesses is" in result


def test_handle_guess_invalid():
    result = handle_guess("abc")
    assert "Invalid query. Please enter a number." in result


def test_handle_guess_correct():
    global secret_number
    secret_number = 50
    result = handle_guess("50")
    assert "Correct!" in result


def test_handle_guess_no_remaining_guesses():
    global num_g
    num_g = 0
    result = handle_guess("100")
    assert "Unlucky! No remaining guesses." in result
