from flask import Flask

from src.repositories.movies_repository import MoviesRepository
from src.routes.movies_route import movie_router
from src.configs.database import Configs, db


# Create the application instance.
# __name__ is the name of the current Python module.
app = Flask(__name__)

app.register_blueprint(movie_router, url_prefix='/movies')

app.config.from_object(Configs)

db.init_app(app)


@app.before_first_request
def before_first_request():

    with app.app_context():
        db.create_all()

    MoviesRepository().populate_database()


# If app.py is run directly, start the server.
if __name__ == '__main__':
    app.run()