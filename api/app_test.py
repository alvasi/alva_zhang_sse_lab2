import unittest
from flask_testing import TestCase
from your_flask_app import app


class TestGuessGame(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_guess_equals_num(self):
        with self.client.session_transaction() as session:
            session['num'] = 50
            session['chances'] = 7
        rv = self.client.get('/guess', query_string={'guess': 50})
        self.assert200(rv)
        self.assert_template_used('result.html')
        self.assertIn('Hurray! You got it in {} steps!'
                      .format(7 - 7), rv.data.decode())

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
            session['chances'] = 0
        rv = self.client.get('/guess', query_string={'guess': 25})
        self.assert200(rv)
        self.assert_template_used('result.html')
        self.assertIn('Phew! You lost the game. You are out of chances',
                      rv.data.decode())


if __name__ == '__main__':
    unittest.main()
