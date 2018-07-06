"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer.

    Janet|Jefferson|janet@hotmail.com|seekrit"""

    def __init__(self, first, last, email, password):
        self.first = first
        self.last = last
        self.email = email
        self.password = password


def get_customers_from_txt(filepath):
    customer_list = []
    with open(filepath) as file:
        for line in file:
            line = line.rstrip()
            customer_data = line.split('|')
            first, last, email, password = customer_data
            new_customer = Customer(first, last, email, password)
            customer_list.append(new_customer)

    return customer_list


def get_by_email(filepath, email):
    customer_list = get_customers_from_txt(filepath)
    for customer in customer_list:
        if customer.email == email:
            return customer

    return None
