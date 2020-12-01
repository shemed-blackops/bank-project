import re
import random
from datetime import datetime


class Account:
    def __init__(self):
        self.account_no = self.generate_account_no()
        self.account_balance = 0

    def generate_account_no(self):
        # Genrating account number
        first_chunk = str(random.randint(1000, 9999))
        second_chunk = str(random.randint(1000, 9999))
        cvc = str(random.randint(100, 999))
        return f"{first_chunk}{second_chunk}{cvc}"

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        self.account_balance -= amount

    def summary(self):
        return self.account_balance
