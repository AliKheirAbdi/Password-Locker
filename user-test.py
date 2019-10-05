import unittest
from user import User

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    new_user = User("Ali","Kheir","Kh@1234") # captures user details
   
    def setUp(self):
        '''
        setup method that runs before each test cases
        '''
        self.new_user = User("Ali","Kheir","Kh@1234")

    def tearDown(self):
        '''
        teardown method that clean up after each test case has run
        '''
        User.user_details = []


    # test to check correct initialization of user
    def test_init(self):
        '''
        test to check whether user initialized correctly
        '''
        self.assertEqual(self.new_user.first_name,"Ali")
        self.assertEqual(self.new_user.second_name,"Kheir")
        self.assertEqual(self.new_user.password,"Kh@1234")

if __name__ == '__main__':
    unittest.main()
