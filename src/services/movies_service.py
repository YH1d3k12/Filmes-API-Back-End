from src.repositories.movies_repository import MoviesRepository


class MoviesService:


    def __init__(self):
        self.repository = MoviesRepository()


    def get_movies(self):
        """
        Retrieve all movies from repository.

        Returns:
            List[MoviesModel]: List of MoviesModel instances representing movies.
        """

        movies = self.repository.get_movies()
        return movies
    

    def create_movie(self, data):
        """
        Create a new movie in the database.

        Args:
            data (dict): Dictionary containing movie data.

        Returns:
            MoviesModel: The newly created MoviesModel instance.
        """
        
        new_movie = self.repository.create_movie(data)
        return new_movie
    

    def get_producers(self):
        """
        Retrieve producers from repository.

        Returns:
            dict: Dictionary containing producers and their respective movies
        """
        producers = self.repository.get_producers()
        return producers
    

    def get_awards_interval(self):
        result = self.repository.get_awards_interval()
        return result