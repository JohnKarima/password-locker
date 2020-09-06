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
