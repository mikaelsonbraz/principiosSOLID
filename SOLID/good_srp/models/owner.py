from SOLID.good_srp.models.developer import Developer


class Owner(Developer):

    def __init__(self, username, email):
        super().__init__(username, email)

