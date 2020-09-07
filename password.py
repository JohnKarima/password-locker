class User:
    """
    Class that generates new instances of users
    """

    user_list = []

    def __init__(self, usernameU, passwordU):
        self.usernameU = usernameU
        self.passwordU = passwordU

    def save_users(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_users(self):
        '''
        delete_users method to delete saved user objects from user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_username_user(cls, username):
        '''
        method that takes in a username and returns a credential pair that matches that username
        
        Args:
            username
        Returns:
            password
        '''
        for user in cls.user_list:
            if user.usernameU == username:
                return user

    @classmethod
    def user_exists(cls, username, password):
        '''
        Method that checks if a user exists from the user list
        Args:
            number: username to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for User in cls.user_list:
            if User.usernameU == username and User.passwordU == password:
                return True
        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the users list
        '''
        return cls.user_list
    
    @classmethod
    def verify_user(cls,username, password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user = ""
        for user in User.user_list:
            if(user.usernameU == username and user.passwordU == password):
                    a_user == user.usernameU
        return a_user


class Credentials:
    """
    Class that generates new instances of credentials
    """
    credentials_list = []

    def __init__(self, site, username, password):
        self.site = site
        self.username = username
        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credential objects into credentials_list
        '''
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method to delete saved credential objects from credentials_list
        '''
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_site(cls, site):
        '''
        method that takes in a site name and returns a credential pair that matches that site name
        '''
        for credentials in cls.credentials_list:
            if credentials.site == site:
                return credentials

    @classmethod
    def credential_exists(cls, site):
        '''
        Method that checks if a credential exists from the credentials_list
        Args:
            site to search if it exists
        Returns :
            Boolean: True or false depending if the site exists
        '''
        for Credentials in cls.credentials_list:
            if Credentials.site == site:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        '''
        method that returns the credentials list
        '''
        return cls.credentials_list