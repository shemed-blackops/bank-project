from bin.customer import Customer

def main():
    d = {
        'first_name': 'Seleman',
        'last_name' : 'Hemed'
    }
    customer = Customer(d)

    print(customer.get_fullname())



if __name__ == '__main__':
    main()