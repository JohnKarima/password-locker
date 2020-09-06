#!/usr/bin/env python3.8
from password import Credentials

def create_credentials(username, password):
    '''
    function to create  a new credential
    '''
    new_credentials = Credentials(username,password)
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

def find_by_username(username):
    '''
    Function that finds a credential by username and retruns the credential pair
    '''
    return Credentials.find_by_username(username)

def credential_exists(username):
    '''
    function that checks if a credential exists from the credentials list
    '''
    return Credentials.credential_exists(username)

def display_credentials():
    '''
    Function that returns all the saved credentials
    '''
    return Credentials.display_credentials()

def main():
    print("Hello Welcome to password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
            print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential by username, ex -exit the credential list ")

            short_code = input().lower()

            if short_code == 'cc':
                    print("New Credential")
                    print("-"*10)

                    print ("User name ....")
                    u_name = input()

                    print("Password ...")
                    password = input()

                    # print("Phone number ...")
                    # p_number = input()

                    # print("Email address ...")
                    # e_address = input()


                    save_credentials(create_credentials(u_name,password)) # create and save new credentials.
                    print ('\n')
                    print(f"New Credential {u_name} {password} saved!")
                    print ('\n')

            elif short_code == 'dc':

                    if display_credentials():
                            print("Here is a list of all your credentials")
                            print('\n')

                            for credentials in display_credentials():
                                    print(f"{credentials.u_name} {credentials.password} .....")

                            print('\n')
                    else:
                            print('\n')
                            print("You dont seem to have any credentials saved yet")
                            print('\n')

            elif short_code == 'fc':

                    print("Enter the username you want to search for")

                    search_username = input()
                    if credential_exists(search_username):
                            search_credentials = find_by_username(search_username)
                            print(f"{search_credentials.username} {search_credentials.password}")
                            print('-' * 20)

                            # print(f"Username.......{search_contact.phone_number}")
                            # print(f"Password.......{search_contact.email}")
                    else:
                            print("That credential does not exist")

            elif short_code == "ex":
                    print("Bye .......")
                    break
            else:
                    print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()