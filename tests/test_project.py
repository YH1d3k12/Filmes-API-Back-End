import unittest
import json
from flask import Flask

from src.configs.database import db
from src.configs.test_configs import TestConfigs
from src.repositories.movies_repository import MoviesRepository
from src.routes.movies_route import movie_router

class TestApp(unittest.TestCase):


    def setUp(self):
        self.app = Flask(__name__)

        # Test configurations.
        self.app.config.from_object(TestConfigs)

        db.init_app(self.app)

        # Add routes.
        self.app.register_blueprint(movie_router, url_prefix='/movies')

        with self.app.app_context():
            db.create_all()
            
            MoviesRepository().populate_database()


    def tearDown(self):
        # Clears database after test.
        with self.app.app_context():
            db.drop_all()


    def test_get_movies(self):
        with self.app.test_client() as client:
            response = client.get('/movies/')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')

            try:
                json_data = json.loads(response.data)
            except json.JSONDecodeError:    
                self.fail('A resposta não é um JSON válido.')


            # Assert true if JSON data has message and data keys.
            self.assertTrue('message' in json_data)
            self.assertTrue('data' in json_data)

            # Assert true if data is a list.
            self.assertTrue(isinstance(json_data['data'], list))

            # If at least one movie is within data assert True.
            self.assertTrue(len(json_data['data']) > 0)

            # Expected value from the first loaded data.
            expected_movie = {
                "id": 1,
                "year": 1980,
                "title": "Can't Stop the Music",
                "studios": "Associated Film Distribution",
                "producers": "Allan Carr",
                "winner": "yes"
            }

            # Verifies if the first movie has the expected_movie values.
            for key, value in expected_movie.items():
                self.assertEqual(json_data['data'][0][key], value)
                print(f'{key} - {value}')


if __name__ == '__main__':
    unittest.main()