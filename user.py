class User:
    """
    class that generates new user
    """
    user_details = []

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

    # deleting the user account

    def delete_account(self):
        """
        delete account method to remove user account
        """
        User.user_details.remove(self)

    # finding user by first_name
    @classmethod
    def find_by_fname(cls, first_name):
        """
        find user by their first name
        Args:
            first_name: first name of the user to search for
        returns:
            user searched for
        """
        for user in cls.user_details:
            if user.first_name == first_name:
                return user

    # confirm user exist
    @classmethod
    def user_exist(cls, first_name):
        """
        method that checks if the user exists by name
        Args:
        first_name checks if the name exists
        returns a boolean depending if the name exists
        """
        for user in cls.user_details:
            if user.first_name == first_name:
                return True
        return False
    # display user
    @classmethod
    def display_user(cls):
        """
        Function that displays users 
        """

        return cls.user_details()
