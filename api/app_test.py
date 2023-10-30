import unittest
from flask_testing import TestCase
from app import app
from app import process_query


class TestGuessGame(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_guess_equals_num(self):
        with self.client.session_transaction() as session:
            session['num'] = 50
            session['chances'] = 7
        rv = self.client.get('/guess', query_string={'guess': 50})
        self.assertStatus(rv, 302)

    def test_guess_less_than_num(self):
        with self.client.session_transaction() as session:
            session['num'] = 50
            session['chances'] = 7
        rv = self.client.get('/guess', query_string={'guess': 25})
        self.assert200(rv)
        self.assert_template_used('result.html')
        self.assertIn('Your number is less than the random number',
                      rv.data.decode())

    def test_guess_greater_than_num(self):
        with self.client.session_transaction() as session:
            session['num'] = 50
            session['chances'] = 7
        rv = self.client.get('/guess', query_string={'guess': 75})
        self.assert200(rv)
        self.assert_template_used('result.html')
        self.assertIn('Your number is greater than the random number',
                      rv.data.decode())

    def test_no_chances_left(self):
        with self.client.session_transaction() as session:
            session['num'] = 50
            session['chances'] = 1
        rv = self.client.get('/guess', query_string={'guess': 25})
        self.assertStatus(rv, 302)


if __name__ == '__main__':
    unittest.main()


def test_knows_about_dinosaurs():
    assert (
        process_query("dinosaurs") ==
        "Dinosaurs ruled the Earth 200 million years ago"
    )


def test_does_not_know_about_asteroids():
    assert process_query("asteroids") == "Unknown"


def test_knows_name():
    assert process_query("What is your name?") == "AZ"


def test_largest_num():
    assert (
        process_query(
            "Which of the following numbers is "
            "the largest: 61, 98, 68?") == "98"
    )


def test_multiply():
    assert (
        process_query("What is 69 multiplied by 10?") == "690"
    )


def test_squarecube():
    result = process_query(
        "Which of the following numbers is "
        "both a square and a cube: 16, 1, "
        "1315, 125, 1758, 2639, 3720?"
    )
    expected_result = ["1", "125"]
    assert all(item in result for item in expected_result)

