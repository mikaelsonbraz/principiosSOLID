class User:

    def __init__(self, uusername, email):
        self._username = uusername
        self._email = email

    @staticmethod
    def members():
        return ['username1', 'username2', 'username3']
