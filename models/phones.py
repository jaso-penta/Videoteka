

class Phone:
    def __init__(self, phone_number, phone_type):
        self.id = 1
        self.phone_number = phone_number
        self.phone_type = phone_type

    def __str__(self):
        return f'{self.phone_number}; {self.phone_type}'