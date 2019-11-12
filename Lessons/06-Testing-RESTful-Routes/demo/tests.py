from app import app
import unittest

from unittest.mock import Mock

class AppTests(unittest.TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    def test_home_status_code(self):
        # sends HTTP GET request to the application
        # on the specified path
        result = self.app.get('/') 

        # assert the status code of the response
        self.assertEqual(result.status_code, 200)

    def test_fortune_results_default_response(self):
        result = self.app.get('/fortune_results')

        self.assertIn('Nothing of note', str(result.data))

    def test_fortune_results_unicorn(self):
        result = self.app.get('/fortune_results?animal=unicorn')

        self.assertIn('magical day', str(result.data))

    def test_fortune_results_cat(self):
        result = self.app.get('/fortune_results?animal=cat')

        self.assertIn('will be paw-some', str(result.data))



# run the tests
if __name__ == '__main__':
    unittest.main()