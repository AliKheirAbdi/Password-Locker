class User:
    '''
    this class generates the new instaces of a user
    '''
    user_details = []

    def __init__(self,first_name,second_name,password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password

        def __init__(self, first_name, second_name, password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password
    # This saves a new user registration

    def save_user(self):

        """
        this save method adds and stores our user
        """
        User.user_details.append(self)
        
    '''
        save method that adds stores our user
        '''
        User.user_details.append(self) 
        User.user_details.append(self)
        
    # deleting the user account
    def delete_account(self):
        '''
        delete account method to remove user account
        '''
        User.user_details.remove(self)     