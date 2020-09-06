import unittest
from password import User
from password import Credentials

class TestPassword(unittest.TestCase):
    '''
    Test class that defines the test cases for the Credentials class behaviours
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credentials = Credentials("montecarlos", "2bornot2b")

    def test_init(self):
        '''
        test_init case to see in th eobject is initialized properly
        '''
        self.assertEqual(self.new_credentials.username,"montecarlos")
        self.assertEqual(self.new_credentials.password,"2bornot2b")

if __name__ == "__main__":
    unittest.main
