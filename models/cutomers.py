


class Customer:
    def __init__(self, name, surname, phone, email, postal_adress):
        self.id = 1
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email
        self.postal_adress = postal_adress
        self.rented_movies = []

    def add_movie(self, movie):
        self.rented_movies.append(movie)

    def __str__(self):
        return f'\n{self.name} {self.surname}\n{self.phone}\n{self.email}\n{self.postal_adress}'
