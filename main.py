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
    choice = input('> ')
    if choice == '1':
        menu_new_user()
        # For new user
        # Taking user input
        # details = {}
        choice = input('> ')
        if choice == '1':
            first_name = input('First Name: ')
            last_name = input('Last Name: ')
            phone_number = input('Phone Number: ')

            # Adding to details
            details = {
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number
            }
            # Insert customer data
            customer.insert_data(details)

    # Existing user
    elif choice == '2':
        print('Account Number: ')
        account_number = input('> ')

        menu_existing_user()
        choice = input('> ')
        if choice == '1':
            # Fetch account details
            summary = customer.account_summary(account_number)
            print(summary)
        elif choice == '2':
            print('Amount: ')
            amount = float(input('> '))
            result = customer.deposit(account_number, amount)
            print(result)
            summary = customer.account_summary(account_number)
            print(summary)
        elif choice == '3':
            print('Amount')
            amount = float(input('> '))
            result = customer.withdraw(account_number, amount)
            print(result)
            summary = customer.account_summary(account_number)
            print(summary)


if __name__ == '__main__':
    main()
