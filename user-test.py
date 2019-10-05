import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    new_user = User("Ali","Kheir","Kh@1234") # captures new user details
    def setUp(self):
        '''
        setup method that runs before each test cases
        '''
        self.new_user = User("Ali","Kheir","Kh@1234")
