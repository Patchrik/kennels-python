EMPLOYEES = [
    {"id": 1, "name": "John Smith", "department": "Accounting"},
    {"id": 2, "name": "Jacob Williams", "department": "Human Resources"},
    {"id": 3, "name": "Trevor Lockwood", "department": "Product Development"},
    {"id": 4, "name": "Ben Grant", "department": "Marketing"},
    {"id": 5, "name": "Chad Davidson", "department": "Engineering"},
]


def get_employee_by_id(id: str):
    """Returns a single employee object based on the provided ID."""
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def get_employees():
    '''Returns a list of all employees and takes no parameters'''
    return EMPLOYEES
