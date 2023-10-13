from flask import Blueprint

from src.controllers.movies_controller import MoviesController


movie_router = Blueprint('movies', __name__)

controller = MoviesController()


@movie_router.route('/', methods=['GET'])
def get_movies():
    return controller.get_movies()


@movie_router.route('/', methods=['POST'])
def create_movie():
    return controller.create_movie()