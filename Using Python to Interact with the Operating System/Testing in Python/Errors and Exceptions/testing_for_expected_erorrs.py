# With some edge cases like negative value of minlen the expectation is that the function will raise an error& we want to be able to test that too
# To achieve that we use assertRaises method provided by the unittest module


import unittest

from raisingerrors import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user("validuser", 3), True)

    def test_too_short(self):
        self.assertEqual(validate_user("inv", 5), False) 
    
    def test_invalid_characters(self):
        self.assertEqual(validate_user("invalid_user", 1), False) 

    # Add test cases:
    def test_invalid_minlen(self):
        self.assertRaises(ValueError, validate_user, "user", -1)


# Run the tests
unittest.main()              