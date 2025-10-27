import json
from shared import FILE_PATH_ROOT
from models import Movie


class MovieRepository:
    def __init__(self, file_path=FILE_PATH_ROOT + "movies.json"):
        self.file_path = file_path
        self.movies = self.get_all_movies()
    

    def save_movie(self, movie: Movie):
        movie.id = self.get_id()
        self.movies.append(movie)
        movies_dicts = [self.movie_to_dict(movie) for movie in self.movies]
        with open(self.file_path, 'w') as file_writer:
            json.dump(movies_dicts, file_writer, indent=4)

        
    def get_all_movies(self):
        try:
            with open(self.file_path, 'r') as file_reader:
                self.movies = json.load(file_reader)
                return [self._dict_to_movie(movie) for movie in self.movies]
        except FileNotFoundError:
            print(f'File not found: {self.file_path}')
            return []
        except Exception as ex:
            print(f'Error reading movies from file: {ex}')
            return []



    # def add_movie(self):
    #     title = input('Unesite naslov filma: ')
    #     director = input('Unesite redatelja: ')
    #     actors = input('Unesite glumce: ')
    #     year = int(input('Unesite godinu: '))

    #     movie = Movie(self, title, director, actors, year)
    #     self.movies.append(movie)
    #     print(f'Film "{title}" je dodan u biblioteku.\n')
    #     next_movie = input('Zelite li unjeti novi film? (da/ne): ').lower()
    #     if next_movie == 'da':
    #         self.add_movie()

    
    
    def find_movie_by_name(self, title):
        for movie in self.movies:
            if movie.title.lower() == title.lower():
                return movie
        return None
        
  

    def _dict_to_movie(self, movie_dict: dict):
        return Movie(self.get_id(),
                     movie_dict['title'],
                     movie_dict['director'],
                     movie_dict['actors'],
                     movie_dict['year'])
    

    def movie_to_dict(self, movie: Movie):
        return {
            'id': movie.id,
            'title': movie.title,
            'director': movie.director,
            'actors': movie.actors,
            'year': movie.year
        }


    def get_id(self) -> int:
        if len(self.movies) == 0:
            return 1
        else:
            return self.movies[-1].id + 1