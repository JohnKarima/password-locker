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
        test_init case to see in the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.username,"montecarlos")
        self.assertEqual(self.new_credentials.password,"2bornot2b")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run
        '''
        Credentials.credentials_list = []

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into the credentials list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials objects into the credentials_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("boba", "tea")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("boba", "tea")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
    unittest.main
