from bin.customer import Customer
from bin.db import DB


def print_banner():
    banner = """
        *********************************
        *       Blackops Bank PLC       *
        *********************************
        """
    print(banner)


def print_menu():
    menu = """
        *********************************
        *           MENU                *
        *********************************
        *       1. Check Balance        *
        *       2. Deposit              *
        *       3. Withdraw             *
        *********************************
    """
    print(menu)


def main():
    # Printing banner and Menu
    print_banner()
    print_menu()

    # Taking user input
    details = {}
    first_name = input('First Name: ')
    last_name = input('Last Name: ')
    phone_number = input('Phone Number: ')

    # Adding to details
    details = {
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number
    }

    # Creating customer
    customer = Customer(details)

    # Creating database object
    db = DB()
    print(db)


if __name__ == '__main__':
    main()
