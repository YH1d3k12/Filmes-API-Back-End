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
        """
        Gets all producers individualy with their respective movies, based on movies.

        Returns:
            dict: Dictionary containing producers and their respective movies.
        """
        # Gets movies from database.
        movies = self.get_movies()

        # Defaultdict is used to only create a new key if the key is not found.
        # That way, if a producer already exists, the value is associate with the producer key.
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
    

    def get_awards_interval(self):
        """
        Gets the interval between awards from producers.

        Returns:
            dict: Dictionary containing the top three producers with the minimum and maximum interval.
        """
        producers_data = self.get_producers()

        # Dictionary to store the intervals for each producer.
        producer_intervals = defaultdict(list)

        for producer, movies in producers_data.items():
            winning_movies = [movie for movie in movies if movie['winner'] == 'yes']

            if len(winning_movies) >= 2:
                # lambda is a anonymous function that takes a variable `x` and returns `x['year']`.
                winning_movies.sort(key=lambda x: x['year'])

                # This loop iterates over the indices of the movies list, excluding the last index.
                intervals = [
                    movies[i + 1]['year'] - movies[i]['year'] 
                    for i in range(len(movies) - 1)
                ]

                # Find intervals between awards.
                if intervals:
                    min_interval = min(intervals)
                    min_index = intervals.index(min_interval)

                data = {
                    'interval': min_interval,
                    'previousWin': movies[min_index]['year'],
                    'followingWin': movies[min_index + 1]['year'],
                }
                producer_intervals[producer].append(data)
                
        # Sort producers by interval and get the top three.
        top_producers_min = sorted(
            producer_intervals.items(),
            key=lambda x: x[1][0]['interval']
        )[:3]  # Get the top three with the minimum interval.

        top_producers_max = sorted(
            producer_intervals.items(),
            key=lambda x: x[1][0]['interval'],
            reverse=True
        )[:3]  # Get the top three with the maximum interval.

        result = {
            "min": [
                {
                    'producer': producer,
                    **data[0]
                }
                for producer, data in top_producers_min
            ],
            "max": [
                {
                    'producer': producer,
                    **data[0]
                }
                for producer, data in top_producers_max
            ]
        }

        return result
    

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