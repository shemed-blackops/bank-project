import random
from bin.db import Database


class Account:
    def __init__(self):
        self.account_no = self.generate_account_no()
        self.account_balance = 0

    @staticmethod
    def generate_account_no():
        # Generating account number
        first_chunk = str(random.randint(1000, 9999))
        second_chunk = str(random.randint(1000, 9999))
        cvc = str(random.randint(100, 999))
        return f"{first_chunk}{second_chunk}{cvc}"

    def deposit(self, account_no, amount):
        db = Database().connect()
        c = db.cursor()
        deposit_query = """
        UPDATE account
        SET account_balance = account_balance + %s
        WHERE account.account_no = %s
        """
        deposit_data = (amount, account_no)
        c.execute(deposit_query, deposit_data)
        db.commit()
        c.close()
        db.close()
        return 'Amount Deposit successfully'

    def withdraw(self, account_no, amount):
        db = Database().connect()
        c = db.cursor()
        withdraw_query = """
               UPDATE account
               SET account_balance = account_balance - %s
               WHERE account.account_no = %s
               """
        withdraw_data = (amount, account_no)
        c.execute(withdraw_query, withdraw_data)
        db.commit()
        c.close()
        db.close()
        return 'Amount withdraw successfully'
