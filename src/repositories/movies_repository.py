import pandas as pd
import re
from collections import defaultdict

from src.utilities.movies_verification import MoviesVerification
from src.models.movies_model import MoviesModel
from src.configs.database import db


class MoviesRepository:


    def get_movies(self):
        """
        Retrieve all movies from database.

        Returns:
            List[MoviesModel]: List of MoviesModel instances representing movies.
        """
        movies = MoviesModel.query.all()
        return movies
    

    def create_movie(self, data):
        """
        Create a new movie in the database.

        Args:
            data (dict): Dictionary containing movie data.

        Returns:
            MoviesModel: The newly created MoviesModel instance.
        """

        new_movie = MoviesModel(
            year = data['year'],
            title = data['title'],
            studios = data['studios'],
            producers = data['producers'],
            winner = MoviesVerification.verify_winner_value(data)
        )

        db.session.add(new_movie)
        db.session.commit()

        return new_movie
    
    
    def get_producers(self):
        # Gets movies from database.
        movies = self.get_movies()

        producers_data = defaultdict(list)

        for movie in movies:
            producers = re.split(', | and ', movie.producers)
            for producer in producers:
                data = {
                    'title': movie.title,
                    'year': movie.year,
                    'winner': 'yes' if movie.winner else 'no'
                }
                producers_data[producer].append(data)

        return producers_data

    def populate_database(self):
        """
        Populate database with movies from movielist.csv file.
        """
        if not MoviesModel.query.first():
            df = pd.read_csv('src/data/movielist.csv', delimiter=';', header=0)

            for index, row in df.iterrows():

                data = {
                    'year': int(row['year']),
                    'title': row['title'],
                    'studios': row['studios'],
                    'producers': row['producers'],
                    'winner': row['winner']
                }

                self.create_movie(data)