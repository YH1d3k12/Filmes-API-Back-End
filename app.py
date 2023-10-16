from flask import Flask

from src.repositories.movies_repository import MoviesRepository
from src.configs.database import db
from src.configs.app_configs import AppConfigs
from src.routes.movies_route import movie_router

# Create an instance of the application.
# __name__ is the name of the current Python module (the file name).
app = Flask(__name__)

# App routes.
app.register_blueprint(movie_router, url_prefix='/movies')

# App configurations.
app.config.from_object(AppConfigs)

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