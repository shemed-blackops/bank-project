from mysql.connector import cursor
from bin.account import Account
from bin.db import Database
from textwrap import dedent


class Customer(Account):
    def __init__(self):
        super().__init__()
        self.details = {}
        self.fullname = self.get_fullname()
        self.account_no = Account().generate_account_no()

    def get_fullname(self):
        return f"{self.details.get('first_name')} {self.details.get('last_name')}"

    def initial_account_details(self):
        output = f"""
               ***************************************
               Name : {self.get_fullname()}
               Account No: {self.account_no}
               Account Balance: {self.account_balance} 
               ****************************************
               """
        return dedent(output)

    def account_summary(self, account_no):
        db = Database().connect()
        c = db.cursor()

        summary_query = """
        SELECT 
        customer.fullname, customer.account_no, account.account_balance 
        FROM customer
        INNER JOIN 
        account
        WHERE customer.account_no = account.account_no
        AND customer.account_no = %s
        """

        summary_data = (account_no,)
        # executing query
        c.execute(summary_query, summary_data)
        summary = c.fetchone()
        fullname, account_no, account_balance = summary

        output = f"""
        ***************************************
        Name : {fullname}
        Account No: {account_no}
        Account Balance: {account_balance} 
        ****************************************
        """
        c.close()
        db.close()
        return dedent(output)

    def insert_data(self, details):
        self.details = details
        customer_query = """INSERT INTO customer(fullname, phone_number, account_no) VALUES (%s, %s, %s)"""
        customer_data = (self.get_fullname(), self.details.get('phone_number'), self.account_no)
        account_query = """INSERT INTO account(account_no, account_balance) VALUES (%s, %s)"""
        account_data = (self.account_no, self.account_balance)

        # Database object
        db = Database().connect()
        c = db.cursor()
        c.execute(account_query, account_data)  # Insert into account first
        c.execute(customer_query, customer_data)
        db.commit()
        c.close()
        db.close()

    def check_account_no(self, account_number):
        db = Database().connect()
        c = db.cursor()
        check_sql = """
        SELECT account_no
        FROM customer
        WHERE account_no = %s
        """
        check_data = (account_number,)
        c.execute(check_sql, check_data)
        result = c.fetchone()
        return result
