CUSTOMERS = [
    {"id": 1, "name": "John Smith", },
    {"id": 2, "name": "Jacob Williams", },
    {"id": 3, "name": "Trevor Lockwood", },
    {"id": 4, "name": "Ben Grant", },
    {"id": 5, "name": "Chad Davidson", },
]


def get_customer_by_id(id: str):
    """Returns a single customer object based on the provided ID."""
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer


def get_customers():
    '''Returns a list of all employees and takes no parameters'''
    return CUSTOMERS


def create_customer(customer):
    '''This function creates a new customer object based on the provided customer dict'''
    new_id = CUSTOMERS[-1]['Id'] + 1
    customer['id'] = new_id
    CUSTOMERS.append(customer)
    return customer
