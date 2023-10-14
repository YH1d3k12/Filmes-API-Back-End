from src.models.movies_model import MoviesModel
from src.configs.database import db
from src.utilities.movies_verification import MoviesVerification


class MoviesRepository:


    def get_movies(self):
        movies = MoviesModel.query.all()
        return movies
    

    def create_movie(self, data):
        # Verifies if winner exist in data. If not, set winner as False.
        

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