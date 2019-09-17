# test_greeting.py
# Import in the Python unittest library
import unittest

# Declare our function
def greet_by_name(name):
  greeting = "Hello, " + name + "!"
  return greeting

# Q: What's the class keyword mean here? 
# A: You'll find out in the CS OOP classes coming soon!
# For now, know that your tests must look like this.
class GreetByNameTests(unittest.TestCase):
    # For each test in the class, make a method where self is the parameter
    def test_default_greeting(self):
        # the actual test
        self.assertEqual(greet_by_name('Dani'), 'Hello, Dani!')

# run the tests
if __name__ == '__main__':
    unittest.main()