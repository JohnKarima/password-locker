class User:
    """
    Class that generates new instances of users
    """

    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    pass

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





