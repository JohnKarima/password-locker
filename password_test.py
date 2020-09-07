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
        test_delete_users to test if we can remove a user from our user list
        '''
        self.new_user.save_users()
        test_user = User("Mandem", "uleule")
        test_user.save_users()
        self.new_user.delete_users()
        self.assertEqual(len(User.user_list),1)

    def test_user_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the user
        '''
        self.new_user.save_users()
        test_user = User("Mandem", "uleule")
        test_user.save_users()

        user_exists = User.user_exists("Mandem", "uleule")
        self.assertTrue(user_exists)

    def test_find_users_by_username(self):
        '''
        test to check if we can find the needed username and password combination whiile searching by username
        '''
        self.new_user.save_users()
        test_user = User("Mandem", "uleule")
        test_user.save_users()
        found_user = User.find_by_username_user("Mandem")

        self.assertEqual(found_user.usernameU,test_user.usernameU)

    def test_display_all_users(self):
        '''
        method that returns a list of all users saved
        '''
        self.assertEqual(User.display_users(),User.user_list)


class TestPassword(unittest.TestCase):
    '''
    Test class that defines the test cases for the Credentials class behaviours
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases
        '''
        self.new_credentials = Credentials("twitter", "montecarlos", "2bornot2b")

    def test_init(self):
        '''
        test_init case to see in the object is initialized properly
        '''
        self.assertEqual(self.new_credentials.site,"twitter")
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
        test_credentials = Credentials("finsta", "boba", "tea")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credentials to test if we can remove a credential from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("finsta", "boba", "tea")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_find_credentials_by_site(self):
        '''
        test to check if we can find the relevant username and password combination whiile searching by username
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("finsta", "boba", "tea")
        test_credentials.save_credentials()
        found_credentials = Credentials.find_by_site("finsta")

        self.assertEqual(found_credentials.username,test_credentials.username)

    def test_credentials_exists(self):
        '''
        test to check if we can return a Boolean if we cannot find the credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("finsta", "boba", "tea")
        test_credentials.save_credentials()

        credential_exists = Credentials.credential_exists("finsta")
        self.assertTrue(credential_exists)

    def test_display_all_credentials(self):
        '''
        method that returns a list of all credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)
        
if __name__ == "__main__":
    unittest.main
