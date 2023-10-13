from src.repositories.movies_repository import MoviesRepository


class MoviesService:


    def __init__(self):
        self.movies_repository = MoviesRepository()


    def get_movies(self):
        movies = self.movies_repository.get_movies()
        return movies
    

    def create_movie(self, data):
        return self.movies_repository.create_movie(data)