import unittest

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']

def get_compliment():
    compliment = compliments[0]
    return f'Hello there, user! You are so {compliment}!'

class ComplimentTests(unittest.TestCase):
    # For each test in the class, make a method where self is the parameter
    def test_compliment(self):
        # the actual test
        self.assertEqual(get_compliment(), 'Hello there, user! You are so coolio!')

# run the tests
if __name__ == '__main__':
    unittest.main()