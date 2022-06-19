from SOLID.good_srp.models.user import User


class Developer(User):

    def __init__(self, username, email):
        super().__init__(username, email)

    @staticmethod
    def members():
        return ['username1', 'username2', 'username3']

    @staticmethod
    def work():
        return "Coding..."