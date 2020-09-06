#!/usr/bin/env python3.8
from password import User
from password import Credentials

def create_users(username, password):
    '''
    function to create  a new user
    '''
    new_user = User(username,password)
    return new_user

def save_users(user):
    '''
    Function to save users
    '''
    user.save_users()

def delete_users(user):
    '''
    Function to delete a user
    '''
    user.delete_users()

def user_exists(username, password):
    '''
    function that checks if a user exists from the user list
    '''
    return User.user_exists(username, password)

def find_by_username_user(username):
    '''
    Function that finds a user by username 
    '''
    return User.find_by_username_user(username)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

# def login_user(username,password):
#     """
#     function that checks whether a user exists and then logs in the user.
#     """
  
#     check_user = User.verify_user(username,password)
#     return check_user







def create_credentials(site, username, password):
    '''
    function to create  a new credential
    '''
    new_credentials = Credentials(site, username,password)
    return new_credentials

def save_credentials(credentials):
    '''
    Function to save credentials
    '''
    credentials.save_credentials()

def delete_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def find_by_site(site):
    '''
    Function that finds a credential by username and returns the credential pair
    '''
    return Credentials.find_by_site(site)

def credential_exists(site):
    '''
    function that checks if a credential exists from the credentials list
    '''
    return Credentials.credential_exists(site)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to password locker.") 
    print("Let's get you started by creating your new account")
    print("-"*10)

    print("Please input a Password_Locker UserName of your choice...")
    u_name_login = input()

    print("Please input the Password_Locker Password you'll be using...")
    password_login = input()

    save_users(create_users(u_name_login,password_login)) 
    print ('\n')
    print(f"New User username: {u_name_login} password: {password_login} saved!")

    print("Here is a list of all the users")
    print('\n')

    for user in display_users():
        print(f"{user.usernameU}, ThomasReaddead, IanMoletown, AngelicahDafoe.....")
        print ('\n')

        break

    print("Great! Now let's login to Password_Locker")
    print("-"*10)
    print("Enter your User name and your Password to log in:")
    username = input("Username: ")
    password = input("Password: ")
    

    login = user_exists(username,password)

    if login == True :
        print(f"Hello {username}. Welcome To Password_Locker")  
        print('\n')
    elif login == False :
        print("Please try again")

    

    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential by username, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("Site name ....")
                    s_name = input()

                    print ("User name ....")
                    u_name = input()

                    print("Password ...")
                    password = input()

                    save_credentials(create_credentials(s_name, u_name,password)) 
                    print ('\n')
                    print(f"New Credential for {s_name} account:\n Username: {u_name}\n Password: {password}")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your credentials:")
                            print('\n')

                            for credentials in display_credentials():
                                    print(f" Site: {credentials.site} Username: {credentials.username} Password: {credentials.password} .....")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the site name you want to search for")

                    search_site = input()
                    if credential_exists(search_site):
                            search_credentials = find_by_site(search_site)
                            print(f"Found. Site: {search_credentials.site} Username: {search_credentials.username} Password: {search_credentials.password}")
                            print('-' * 20)

                    else:
                            print("That credential does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()