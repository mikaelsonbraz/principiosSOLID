class User:

    def __init__(self, username, email):
        self._username = username
        self._email = email

    @staticmethod
    def work():
        raise NotImplementedError

    @property
    def getUsername(self):
        return self._username

    @property
    def getEmail(self):
        return self._email
