#!/usr/bin/env python3.8
from password import User, Credentials
import pyfiglet, pyperclip

ascii_banner = pyfiglet.figlet_format("Pass Lock!")
print(ascii_banner)

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
    Function that finds a credential by site and returns the credentials
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
    print("Hello Welcome to Password_Locker.") 
    print("Let's get you started by creating your new account")
    print("="*50)

    print("Please input a Password_Locker UserName of your choice...")
    u_name_login = input()
    print("Please input the Password_Locker Password you'll be using...")
    password_login = input()

    save_users(create_users(u_name_login,password_login)) 
    print ('\n')
    print(f"New User Username: {u_name_login}, with Password: {password_login}, saved!")
    print("Now let's login to Password_Locker")
    print("="*50)
    print("Enter your Username and your Password to log in:")
    username = input("Username: ")
    password = input("Password: ")

    if user_exists(username, password):
        login = user_exists(username,password)
        print('\n')
        print(f"Hello {username}. Welcome To Password_Locker!")

    else:
        while user_exists(username,password) == False:
            print('\n')
            print("Wrong Password_Locker login Credentials!")
            print("Please try again")
            print('\n')

            username = input("Username: ")
            password = input("Password: ")
            login = user_exists(username,password)
        
    while login == True:
        print('\n')
        print("Use these short codes to : \ncc -Create a new credential, dc -Display credentials, \nfc -Find a credential by site, d -Delete a credential by site, \nex -Exit Password_Locker")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("="*50)

            print ("Site name ....")
            s_name = input()

            print ("User name ....")
            u_name = input()

            print("Password ...")
            password = input()

            save_credentials(create_credentials(s_name, u_name,password)) 
            print('\n')
            print(f"New Credential for -{s_name} account:\n Username: {u_name}\n Password: {password} created")
            print("="*50)

        elif short_code == 'dc':

            if display_credentials():

                print("Here is a list of all your credentials:")
                print('\n')

                for credentials in display_credentials():

                    print(f" Site: {credentials.site} Username: {credentials.username} Password: {credentials.password} .....")
                    print("-"*50)

            else:
                print('\n')
                print("You don't seem to have any credentials saved yet")
                print("="*50)
                print('\n')

        elif short_code == 'fc':

            print("Enter the site name you want to search for")

            search_site = input()
            if credential_exists(search_site):
                search_credentials = find_by_site(search_site)
                print('\n')
                print(f"Found. Site: {search_credentials.site} Username: {search_credentials.username} Password: {search_credentials.password}")
                print('=' *50)

            else:
                print("That credential does not exist")
                print("="*50)

        elif short_code == "d":
            print("Enter the account site name of the credentials you want to delete")
            search_name = input().lower()
            if find_by_site(search_name):
                search_credential = find_by_site(search_name)
                print("="*50)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.site} have successfully been deleted!!!")
                print('\n')

            else:
                print("That Credential you want to delete does not exist in your store yet")

        elif short_code == "ex":
            ascii_banner = pyfiglet.figlet_format("Bye Bye!")
            print(ascii_banner)
            print("See you again .......")
            break

        else:
            print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()