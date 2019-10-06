#!/usr/bin/env python3.6
from user import User
from credentials import Credentials
from tkinter import *

# creating an account
def create_user(fname,sname,password):
    """
    function to create a new user account
    """
    new_user = User(fname,sname,password)
    return new_user

def create_app(app,app_password):
    """
    Function to create new app and password
    """
    new_app = Credentials(app,app_password)
    return new_app
