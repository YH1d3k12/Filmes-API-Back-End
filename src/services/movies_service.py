from src.repositories.movies_repository import MoviesRepository


class MoviesService:


    def __init__(self):
        self.movies_repository = MoviesRepository()


    def get_movies(self):
        """
        Retrieve all movies from repository.

        Returns:
            List[MoviesModel]: List of MoviesModel instances representing movies.
        """

        movies = self.movies_repository.get_movies()
        return movies
    

    def create_movie(self, data):
        """
        Create a new movie in the database.

        Args:
            data (dict): Dictionary containing movie data.

        Returns:
            MoviesModel: The newly created MoviesModel instance.
        """
        
        new_movie = self.movies_repository.create_movie(data)
        return new_movie