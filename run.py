#!/usr/bin/env python3.8
from password import Credentials

def create_credentials(username, password):
    '''
    function to create  a new credential
    '''
    new_credential = Credentials(username,password)
    return new_credential
    