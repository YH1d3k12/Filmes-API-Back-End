from flask import Flask

from src.repositories.movies_repository import MoviesRepository
from src.routes.movies_route import movie_router
from src.configs.database import Configs, db

# Create an instance of the application.
# __name__ is the name of the current Python module (the file name).
app = Flask(__name__)

app.register_blueprint(movie_router, url_prefix='/movies')

# Sets the app configuration from Configs.
app.config.from_object(Configs)

db.init_app(app)


# Before the first request, create the database tables.
@app.before_first_request
def before_first_request():
    # `app` is an instance of Flask, so we can use the `app_context()` method to get a context.
    # Contesxt grants access to app configuration and resources.
    # `with` is used to guarantee that the context is released when the block ends.
    with app.app_context():
        db.create_all()

    MoviesRepository().populate_database()


# If app.py is run directly, start the server.
if __name__ == '__main__':
    app.run()