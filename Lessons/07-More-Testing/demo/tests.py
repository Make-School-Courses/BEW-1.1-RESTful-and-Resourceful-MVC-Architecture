from app import app
from unittest import TestCase, main
from unittest.mock import patch, ANY

class AppTests(TestCase): 

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True 

    @patch('app.requests')
    def test_weather_results(self, requests):
        requests.get().json.return_value = {
            'main': {
                'temp': 60
            }
        }
        result = self.app.get('/weather_results?city=San+Francisco')
        self.assertEqual(result.status_code, 200)

        page_content = result.get_data(as_text=True)
        self.assertIn('It is now 60 degrees Fahrenheit', page_content)

        requests.get.assert_called_with(ANY, 
            params={'q': 'San Francisco', 'units': 'Imperial', 'appid': ANY})

# run the tests
if __name__ == '__main__':
    main()