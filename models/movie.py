

class Movie:
    def __init__(self, title, director, actors, year):
        self.id = 1
        self.title = title
        self.director = director
        self.actors = actors
        self.year = year

    def __str__(self):
        return f'{self.title} - {self.director} - {self.actors} - {self.year}'
    