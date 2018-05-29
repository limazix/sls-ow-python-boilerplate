import json
import unittest
from handler import hello

class MainTestCase(unittest.TestCase):
    """ Class to test hello function
    """

    def test_greeting_given_person(self):
        """ It should return a dictionary with key 'greeting' and value 'Hello <name>!' if a name is provided
        """
        result = hello({"name": "Bruno"})
        self.assertDictEqual(result, {"greeting": "Hello Bruno!"})

    def test_greeting_strange_person(self):
        """ It should return a dictionary with key 'greeting' and value 'Hello stranger!' if no name is provided
        """
        result = hello({})
        self.assertDictEqual(result, {"greeting": "Hello stranger!"})

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MainTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
