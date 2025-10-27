from models import (Customer,
                    Movie,
                    RentMovie,
                    Email,
                    PostalAdress,
                    Phone)
from infrastructures import MovieRepository
from infrastructures import CustomerRepository
from infrastructures import EmailsRepository



def main():
    movie_rep = MovieRepository()

    # movie_1 = Movie('The Goodfather', 'Francis Ford Coppola', 'Marlon Brando, Al Pachino', 1972)
    # movie_2 = Movie('The Godfather part II', 'Francis Ford Coppola', 'Al Pachino, Robert Duvall', 1974)
    # movie_3 = Movie('The Godfather part III', 'Francis Ford Coppola', 'Al Pachino,  Diane Keton', 1990)

    # movie_rep.save_movie(movie_1)
    # movie_rep.save_movie(movie_2)
    # movie_rep.save_movie(movie_3)

    email_repo = EmailsRepository()
    email_1 = Email('pero@gmail.com', 'Private')
    email_repo.save_email(email_1)

    customer_repo = CustomerRepository()
    customer_1 = Customer('Pero', 'Peric', '091456789', email_1, 'Zagorska ulica')

    customer_repo.save_customer(customer_1)




    email_repo.edit_email(1)





if __name__ == "__main__":
    main()
