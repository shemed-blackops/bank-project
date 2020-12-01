class Customer:
    def __init__(self, account_no):
        self.account_no = account_no
        self.balance = 0

    def get_fullname(self):
        return f"{self.firstname} {self.surname}"

    def deposit(self, amount):
        self.balance += amount
        return True

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError("Insufficient balance... Please deposit")
        else:
            self.balance -= amount

    def print_summary(self):
        summary = f"""
        Account Name: {self.get_fullname()}
        Account No. :  {self.account_no}
        Balance     : {self.get_balance()}
        """
        return summary
