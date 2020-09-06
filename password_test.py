import unittest
from password import User
from password import Credentials


class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for the User class behaviours
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_user = User("montecarlos1", "2beornot2be")

    def test_init(self):
        '''
        test_init case to see in the object is initialized properly
        '''
        self.assertEqual(self.new_user.usernameU,"montecarlos1")
        self.assertEqual(self.new_user.passwordU,"2beornot2be")

    def tearDown(self):
        '''
        tearDown method that cleans up after each test case has run
        '''
        User.user_list = []

    def test_save_users(self):
        '''
        test_save_user test case to test if the user object is saved into the user list
        '''
        self.new_user.save_users()
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_users(self):
        '''
        test_save_multiple_users to check if we can save multiple user objects into the user_list
        '''
        self.new_user.save_users()
        test_user = User("Mandem", "uleule")
        test_user.save_users()
        self.assertEqual(len(User.user_list),2)

    def test_delete_users(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_user.save_users()
        test_user = User("Mandem", "uleule")
        test_user.save_users()
        self.new_user.delete_users()
        self.assertEqual(len(User.user_list),1)






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

    def test_find_credentials_by_username(self):
        '''
        test to check if we can find the relevant username and password combination whiile searching by username
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("boba", "tea")
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_username("boba")

        self.assertEqual(found_credentials.username,test_credentials.username)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("boba", "tea")
        test_credentials.save_credentials()

        credential_exists = Credentials.credential_exists("boba")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        


if __name__ == "__main__":
    unittest.main
