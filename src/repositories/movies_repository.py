from src.configs.database import db
from src.models.movies_model import MoviesModel


class MoviesRepository:


    def get_movies(self):
        movies = MoviesModel.query.all()
        return movies
    

    def create_movie(self, data):
        # Verifies if winner exist in data. If not, set winner as False.
        if data.get('winner'):
            winner_value = data['winner'].lower() == 'yes' if 'winner' in data else False
        else:
            winner_value = False

        new_movie = MoviesModel(
            year = data['year'],
            title = data['title'],
            studios = data['studios'],
            producers = data['producers'],
            winner = winner_value
        )

        db.session.add(new_movie)
        db.session.commit()

        return new_movie