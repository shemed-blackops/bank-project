from bin.account import Account


class Customer(Account):
    def __init__(self, details):
        super().__init__()
        self.details = details
        self.fullname = self.get_fullname()
        self.account_no = Account().generate_account_no()

    def get_fullname(self):
        return f"{self.details.get('first_name')} {self.details.get('last_name')}"
