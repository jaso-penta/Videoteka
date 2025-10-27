from datetime import datetime


class RentMovie:
    def __init__(self, client, movie, price, rent_date=None):
        self.id = 1
        self.client = client
        self.movie = movie
        self.price: int = price
        self.rent_date = rent_date or datetime.now().strftime('%d.%m.%Y')
        self.rented_titles = [movie.title]
        for movie in self.rented_titles:
            print(f'{movie}')

        self.client.add_movie(self.movie)
        

   

    
    def display_rent(self):
        print(f'Korisnik: {self.client.name} {self.client.surname}')
        print(f'Film: {self.movie.title}')
        print(f'Datum iznajmljivanja: {self.rent_date}')
        print(f'Cijena: {self.price}€')
        print(f'Iznajmljeni sadrzaj: {', '.join(self.rented_titles)}')




    def __str__(self):
        return f'{self.client}, {self.movie}, {self.rent_date}, {self.price}€'
    
