class User:
    """
    Class that generates new instances of users
    """

    user_list = []



    def __init__(self, usernameU, passwordU):
        self.usernameU = usernameU
        self.passwordU = passwordU

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method to delete  saved credential objects from credentials_list
        '''
        Credentials.credentials_list.remove(self)






class Credentials:
    """
    Class that generates new instances of credentials
    """

    credentials_list = []


    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credential objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method to delete  saved credential objects from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_username(cls, username):
        '''
        method that takes in a username and returns a credential pair that matches that username
        
        Args:
            username
        Returns:
            password
        '''
        for credentials in cls.credentials_list:
            if credentials.username == username:
                return credentials

    @classmethod
    def credential_exists(cls, username):
        '''
        Method that checks if a credential exists from the credentials_list
        Args:
            number: username to search if it exists
        Returns :
            Boolean: True or false depending if the credential exists
        '''
        for Credentials in cls.credentials_list:
            if Credentials.username == username:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list






