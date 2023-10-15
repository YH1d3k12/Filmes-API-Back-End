from flask import request, make_response, jsonify

from src.services.movies_service import MoviesService


class MoviesController:


    def __init__(self):
        self.service = MoviesService()


    def get_movies(self):
        """
        Retrieve all movies from service.

        Returns:
            data: Flask response containing a JSON representation of movies.
        """
        movies = self.service.get_movies()
        return make_response(
            jsonify(
                message='Movies retrieved',
                data=[movie.as_dict() for movie in movies]
            ),
            200
        )
    

    def create_movie(self):
        """
        Create a new movie based on the JSON data in the body request.

        Returns:
            Response: Flask response indicating the result of the creation.
        """
        data = {
            'year': request.json.get('year'),
            'title': request.json.get('title'),
            'studios': request.json.get('studios'),
            'producers': request.json.get('producers'),
            'winner': request.json.get('winner')
        }
                
        new_movie = self.service.create_movie(data)

        return make_response(
            jsonify(
                message='Movie created',
                data=new_movie
            ),
            201
        )