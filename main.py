import sys

from bin.customer import Customer
from bin.db import Database


def print_banner():
    banner = """
        *********************************
        *       Blackops Bank PLC       *
        *********************************
        """
    print(banner)


def print_welcome_screen():
    msg = """
    *********************************
    *       1. New User             *
    *       2. Existing User        *
    *********************************
    """
    print(msg)


def menu_new_user():
    new_menu = """
        *********************************
        *           MENU                *
        *********************************
        *       1. Get Account          *
        *********************************
    """
    print(new_menu)


def menu_existing_user():
    existing_menu = """
        *********************************
        *           MENU                *
        *********************************
        *       1. Account Summary      *
        *       2. Deposit              *
        *       3. Withdraw             *
        *********************************
    """
    print(existing_menu)


def main():
    # Printing banner and Menu

    # Create customer object
    customer = Customer()

    print_banner()
    print_welcome_screen()
    choice = clean_data(input('> '))
    if choice == '1':
        menu_new_user()
        # For new user
        # Taking user input
        # details = {}
        choice = clean_data(input('> '))
        if choice == '1':
            first_name = clean_data(input('First Name: '))
            last_name = clean_data(input('Last Name: '))
            phone_number = clean_data(input('Phone Number: '))

            # Adding to details
            details = {
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number
            }
            # Insert customer data
            customer.insert_data(details)

            # Display customer details after registration
            summary = customer.initial_account_details()
            print(summary)
        else:
            print('Wrong choice')
            sys.exit()
    # Existing user
    elif choice == '2':
        print('Account Number: ')
        try:
            account_number = clean_data(input('> '))
            customer.check_account_no(account_number)

        except:
            print('Error occurred')
            sys.exit()

        menu_existing_user()
        choice = clean_data(input('> '))
        if choice == '1':
            # Fetch account details
            summary = customer.account_summary(account_number)
            print(summary)
        elif choice == '2':
            try:
                print('Amount: ')
                amount = float(clean_data(input('> ')))
                result = customer.deposit(account_number, amount)
                print(result)
                summary = customer.account_summary(account_number)
                print(summary)
            except Exception:
                print('Error occurred')
                sys.exit()
        elif choice == '3':
            print('Amount')
            try:
                amount = float(clean_data(input('> ')))
                result = customer.withdraw(account_number, amount)
                print(result)
                summary = customer.account_summary(account_number)
                print(summary)
            except Exception:
                print('Error occured. ')
        else:
            print('Wrong choice')
            sys.exit()
    else:
        print('Wrong choice')
        sys.exit()


def clean_data(data):
    return data.strip()


if __name__ == '__main__':
    main()
