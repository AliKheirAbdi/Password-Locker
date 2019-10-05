class User:
    '''
    this class generates the new instaces of a user
    '''
    user_details = []

    def __init__(self,first_name,second_name,password):
        self.first_name = first_name
        self.second_name = second_name
        self.password = password