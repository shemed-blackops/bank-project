from bin.customer import Customer


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
    print_banner()
    print_menu()


if __name__ == '__main__':
    main()
