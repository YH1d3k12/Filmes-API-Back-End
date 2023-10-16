import unittest
from flask import Flask

from src.configs.database import db
from src.configs.test_configs import TestConfigs
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


    def tearDown(self):
        # Clears database after test.
        with self.app.app_context():
            db.drop_all()


    def test_example(self):
        with self.app.test_client() as client:
            response = client.get('/movies/')
            
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.content_type, 'application/json')


if __name__ == '__main__':
    unittest.main()
