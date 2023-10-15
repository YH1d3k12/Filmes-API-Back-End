from flask import Blueprint

from src.controllers.movies_controller import MoviesController


# The first argument is the name of the Blueprint.
# `__name__`  refer to the current module.
movie_router = Blueprint('movies', __name__)

controller = MoviesController()


@movie_router.route('/', methods=['GET'])
def get_movies():
    """
    Route for retrieving a list of all movies.

    Returns:
        Flask response: JSON representation of movies.
    """
    
    return controller.get_movies()


@movie_router.route('/', methods=['POST'])
def create_movie():
    """
    Route for creating a new movie based on JSON data in the request.

    Returns:
        Flask response: Result of the movie creation.
    """
        
    return controller.create_movie()


@movie_router.route('/producers', methods=['GET'])
def get_producers():
    """
    Route for retrieving producers individualy.

    Returns:
        Flask response: JSON representation of producers.
    """
        
    return controller.get_producers()