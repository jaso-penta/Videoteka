import json
from shared import FILE_PATH_ROOT
from models import Customer
from models import Email


class CustomerRepository:
    def __init__(self, file_path=FILE_PATH_ROOT + "customers.json"):
        self.file_path = file_path
        self.customers = self.get_all_customers()


    def save_customer(self, customer: Customer):
        customer.id = self.get_customer_id()
        self.customers.append(customer)
        customer_dicts = [self.customer_to_dict(customer) for customer in self.customers]
        with open(self.file_path, 'w') as file_writer:
            json.dump(customer_dicts, file_writer, indent=4)


    def get_all_customers(self):
        try:
            with open(self.file_path, 'r') as file_reader:
                self.customers = json.load(file_reader)
                return[self.dict_to_customer(customer) for customer in self.customers]
        except FileNotFoundError:
            print(f'File not found: {self.file_path}')
            return []
        except Exception as ex:
            print(f'Error reading customers from file: {ex}')
            return[]


    def dict_to_customer(self, customer_dict: dict):
        email = Email(
            customer_dict['email']['email_address'],
            customer_dict['email']['email_type']
        )
        return Customer(self.get_customer_id(),
                        customer_dict['name'],
                        customer_dict['surname'],
                        customer_dict['phone'],
                        email,
                        customer_dict['postal_adress']
        )


    def customer_to_dict(self, customer: Customer):
        return {"id": customer.id,
                "name": customer.name,
                "surname": customer.surname,
                "phone": customer.phone,
                "email": {
                    "email_address": customer.email.email_address,
                    "email_type": customer.email.email_type
                },
                "postal_adress": customer.postal_adress}


    def get_customer_id(self) -> int:
        if len(self.customers) == 0:
            return 1
        else:
            return self.customers[-1].id + 1




