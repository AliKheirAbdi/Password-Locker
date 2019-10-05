
class Credentials:
    '''
    class that generates instances of new credentials
    '''
    app_details = []
    
    def __init__(self,app,app_password):
        self.app = app
        self.app_password = app_password
    